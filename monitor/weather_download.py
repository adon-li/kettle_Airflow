import datetime
import requests
import js2py
import datetime
import itertools
from monitor.settings import DATA_SOURCE
from monitor.data_source.engines import  get_engine
import pandas as pd
import numpy as np
from sqlalchemy.orm import sessionmaker, scoped_session
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor
import logging

logger = logging.getLogger('ETL')


class Weather(object):
    def __init__(self):
        self.engine = get_engine(data_source=DATA_SOURCE['vertica_90'])
        self.Session = scoped_session(sessionmaker(bind=self.engine))

    def get_citys(self):
        header = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "Referer": "http://www.weather.com.cn/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        }
        r = requests.get('https://j.i8tq.com/weather2020/search/city.js', headers=header)

        str_back = str(r.content, 'utf-8')

        js_str = ''' 
        function a(){  
            %s;
            return city_data;
        } ''' % str_back
        tt = js2py.eval_js(js_str)
        citys_pack = tt().to_dict()

        citys = []
        for key, value in citys_pack.items():
            citys.extend(
                map(lambda x: {'province': x[0], 'city': x[1], 'area_id': citys_pack[x[0]][x[1]][x[1]]['AREAID']},
                    itertools.product([key], value.keys())))

        today = datetime.datetime.now()
        future_40_day = today + datetime.timedelta(days=40)

        for city in citys:
            city['urls'] = [
                f'''http://d1.weather.com.cn/calendarFromMon/{day.strftime('%Y')}/{city['area_id']}_{day.strftime('%Y%m')}.html'''
                for day in [today, future_40_day]]
        return citys

    def weather_get(self, province, city, url):
        try:
            print('crawl url: %s' % url)
            logger.info('crawl url: %s' % url)
            header = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Host': 'd1.weather.com.cn',
                'Pragma': 'no-cache',
                'Referer': 'http://www.weather.com.cn/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
            }
            r = requests.get(url=url, headers=header, params={'_': str(int(time.time() * 1000))})
            weather_pack = eval(str(r.content, encoding='utf-8').split('=')[1])
            weather_lst = []
            for weather in weather_pack:
                weather_lst.append((province, city, datetime.datetime.now().strftime('%Y-%m-%d'),
                                    datetime.datetime.strptime(weather['date'], '%Y%m%d').strftime('%Y-%m-%d'),
                                    weather['hmin'] if weather['min'] == '' else weather['min'],
                                    weather['hmax'] if weather['max'] == '' else weather['max'],
                                    weather['c1'], weather['c2'], weather['wd1']))

            df = pd.DataFrame(
                columns=['province', 'city', 'total_day', 'weather_day', 'min_tpr', 'max_tpr', 'c1', 'c2',
                         'wind'],
                data=np.array(weather_lst))
            df.to_sql(name='city_weather_40_day', schema='hmcdata', if_exists='append', index=False, con=self.engine)
            df.to_sql(name='city_weather_40_day_history', schema='hmcdata', if_exists='append', index=False, con=self.engine)
            time.sleep(random.randint(5, 8))
            return 'finish'
        except Exception as e:
            logger.error(e)
            print('retry url: %s' % url)
            logger.error('retry url: %s' % url)
            time.sleep(random.randint(12, 30))
            self.weather_get(province, city, url)

    def run(self):
        self.Session.execute(
            f''' delete from hmcdata.city_weather_40_day_history where total_day = '{datetime.datetime.now().strftime('%Y-%m-%d')}' ''')
        self.Session.execute(f''' truncate table hmcdata.city_weather_40_day ''')
        self.Session.commit()
        self.Session.flush()
        crawl_lst = []
        for city in self.get_citys():
            crawl_lst.extend(itertools.product([city['province']], [city['city']], city['urls']))
        with ThreadPoolExecutor(max_workers=5) as e:
            all_task = [e.submit(self.weather_get, p, c, u) for p, c, u in crawl_lst]
            for future in as_completed(all_task):
                logger.info(future.result())

