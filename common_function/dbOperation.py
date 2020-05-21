import pymysql
from getConfigParser import configParse


class DB(object):
    """主要是对数据库的远程操作，查询"""

    def __init__(self, config):
        """
         config = {
                        'host': '127.0.0.1',
                        'port': 3306,
                        'user': 'root',
                        'password': 'zhyea.com',
                        'db': 'employees',
                        'charset': 'utf8mb4',
                        'cursorclass': pymysql.cursors.DictCursor,
                }
        """
        try:
                # 建立链接对象
            self.connection = pymysql.connect(**config,connect_timeout=50)
        except Exception as e:
            print('connect fails!{}'.format(e))
        else:
                # c创建游标对象
            self.cursor = self.connection.cursor()

    def custom_select(self, sql_cmd):
        try:
            self.cursor.execute(sql_cmd)
        except mysql.connector.Error as e:
            print('query error!{}'.format(e))
        else:
            data = self.cursor.fetchall()
            return data
        finally:
            self.cursor.close()
            self.connection.close()

if __name__ == '__main__':
    docker_mysql = configParse(
        "E:/PythonStudy/conf/common_conf", "docker_mysql")
    # host1 = docker_mysql.get_value('host')
    configs = dict()
    config = {'host' : docker_mysql.get_value('host'),
               # 'port' : int(docker_mysql.get_value('port')),
               'port':3307,
               'user' : docker_mysql.get_value('user'),
               'passwd' : docker_mysql.get_value('password'),
               'db' : docker_mysql.get_value('db'),
               'charset' : docker_mysql.get_value('charset'),
               }
    configs = {'host':'192.168.0.103',
              'port':3307,
              'user':'root',
              'passwd':'123456',
              'db':'liyanfeng',
              'charset':'utf8'}
    # config = {'host'='"191.168.0.103"', 'port' = 3307, 'user' = "'root'",
    # 'password' ='123456', 'db': "'liyanfeng'", 'charset': "'utf8'"}
    test1 = DB(config)
    # print(config['host'])
    print(test1)
    print(config)
    print(configs)
    print(type(config))
    print(type(configs))
    # port(config[port])
    if configs == config:
    	print("jelo")
    else:
    	print("no equal")
