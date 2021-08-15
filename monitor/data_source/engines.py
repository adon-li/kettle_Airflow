from .exception import DataBaseConnectError
import sqlalchemy as sa
from urllib.parse import unquote
from sshtunnel import SSHTunnelForwarder
import pymysql

def get_engine(data_source):
    try:
        if data_source['engine'] == 'vertica':
            return sa.create_engine('vertica+vertica_python://{user}:{passwd}@{host}:{port}/{db}'
                                    .format(user=data_source['user'],
                                            passwd=data_source['passwd'],
                                            host=data_source['host'],
                                            port=data_source['port'],
                                            db=data_source['db']))
            # return sa.create_engine('vertica+pyodbc:///?odbc_connect=%s'
            #      %(unquote('''Driver={Vertica};
            #      Database=%s; Servername=%s;
            #      UID=%s; PWD=%s; Port =%s; Locale=zh_CN.utf8''' %(data_source['db'],
            #                                                       data_source['host'],
            #                                                       data_source['user'],
            #                                                       data_source['passwd'],
            #                                                       data_source['port']))))
        elif data_source['engine'] == 'mysql':
            return sa.create_engine('mysql+pymysql://{user}:{passwd}@{host}/{db}?charset=utf8'
                                    .format(user=data_source['user'],
                                            passwd=data_source['passwd'],
                                            host=data_source['host'],
                                            db=data_source['db']))
    except Exception as e:
        raise DataBaseConnectError('executing function "%s.engine" caught %s'%(__name__, e))

def get_ssh_engine(ssh_source, data_source):
    try:
        if data_source['engine'] == 'mysql':
            server = SSHTunnelForwarder((ssh_source['ssh_host'], ssh_source['ssh_port']),
                                        ssh_username=ssh_source['ssh_user'],
                                        ssh_password=ssh_source['ssh_password'],
                                        remote_bind_address=(data_source['host'], data_source['port']))
            server.start()
            local_port = str(server.local_bind_port)
            engine = sa.create_engine('mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}?charset=utf8'
                                   .format(user=data_source['user'],
                                           passwd=data_source['passwd'],
                                           host='127.0.0.1',
                                           port=local_port,
                                           db=data_source['db']))
            return engine
        else:
            raise DataBaseConnectError('could not connect the data_source with ssh!')
    except Exception as e:
        raise DataBaseConnectError('executing function "%s.engine" caught %s' % (__name__, e))

def get_ssh_pymysql(ssh_source,data_source):
    try:
        server = SSHTunnelForwarder((ssh_source['ssh_host'], ssh_source['ssh_port']),
                                    ssh_username=ssh_source['ssh_user'],
                                    ssh_password=ssh_source['ssh_password'],
                                    remote_bind_address=(data_source['host'], data_source['port']))
        server.start()
        local_port = server.local_bind_port
        # print(local_port,data_source['user'],data_source['passwd'],data_source['db'])
        conn = pymysql.connect(host='127.0.0.1', port=local_port, user=data_source['user'], passwd=data_source['passwd'], db=data_source['db'],charset='utf8')
        return conn,server

    except Exception as e:
        raise DataBaseConnectError('executing function "%s.engine" caught %s' % (__name__, e))

def get_pymysql(data_source):
    try:
        # print(local_port,data_source['user'],data_source['passwd'],data_source['db'])
        conn = pymysql.connect(host=data_source['host'], port=data_source['port'], user=data_source['user'], passwd=data_source['passwd'], db=data_source['db'],charset='utf8')
        return conn

    except Exception as e:
        raise DataBaseConnectError('executing function "%s.engine" caught %s' % (__name__, e))
