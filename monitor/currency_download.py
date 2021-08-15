from monitor.settings import DATA_SOURCE
from monitor.data_source.engines import get_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import traceback
import requests
import execjs
class Currency(object):
    def __init__(self):
        self.engine = get_engine(DATA_SOURCE['vertica_90'])
        self.ses = scoped_session(sessionmaker(autocommit=False,
                                  autoflush=False,
                                  bind=self.engine))
    def get_data(self):
        re_html = requests.get('https://www.usd-cny.com/hv.js')
        text = """
        function a(){
        var price = new Object();""" + re_html.text.split('var price = new Object();')[1] + ' return price;}'
        default = execjs.compile(text)
        tt = default.call('a')
        result = {}
        for key in tt:
            if tt[key] != 0:
                result[key.split(':')[0]] = tt['CNY:CUR'] / tt[key]
        return result
    def run_currency(self):
        results = self.get_data()
        try:
            #生成临时表数据数据
            self.ses.execute(f"""truncate table hmcdata.e3_currency_backup;""")
            self.ses.remove()
            for target in results:
                sql1 = f"""INSERT INTO hmcdata.e3_currency_backup(currency_code,exchange_rate) VALUES('{target}',{results[target]});"""
                self.ses.execute(sql1)
                self.ses.commit()
                self.ses.remove()
            #更新正式表，新增历史数据
            sql2 = f"""--   UPDATE hmcdate.e3_curency a SET exchange_rate = b.exchange_rate,gmt_modified=NOW()
--                          FROM hmcdata.e3_currency_backup b where a.currency_code = b.currency_code;
--                          #增加一个insert语法,有就更新,无就新增.
--                          INSERT INTO hmcdata.e3_currency (currency_code,exchange_rate,gmt_modified) 
--                          SELECT currency_code,exchange_rate,NOW() from hmcdata.e3_currency_backup
--                          ON DUPLICATE KEY UPDATE currency_code=VALUES(currency_code),exchange_rate=VALUES(exchange_rate),gmt_modified=NOW()
--  
                        UPDATE hmcdata.e3_currency a SET exchange_rate = t.exchange_rate, gmt_modified = NOW() 
                        FROM (SELECT currency_code, exchange_rate, gmt_created FROM hmcdata.e3_currency_backup) t 
                        where a.currency_code = t.currency_code;
                        
                        INSERT INTO hmcdata.e3_currency (currency_code,exchange_rate,gmt_modified) 
                        SELECT currency_code,exchange_rate,NOW() from hmcdata.e3_currency_backup b
                        WHERE NOT EXISTS (
                        SELECT 1 FROM hmcdata.e3_currency t where b.currency_code =t.currency_code 
                        );
                        
                        DELETE FROM hmcdata.e3_currency_history WHERE DATE(gmt_created) = DATE(NOW());
                        INSERT INTO hmcdata.e3_currency_history (currency_code, currency_name, exchange_rate, gmt_created)
                        SELECT currency_code, currency_name, exchange_rate, gmt_created FROM hmcdata.e3_currency_backup;"""
            self.ses.execute(sql2)
            self.ses.commit()
            self.ses.remove()
        except Exception as e:
            self.ses.rollback()
            traceback.print_exc()
            raise e
        finally:
            self.ses.remove()