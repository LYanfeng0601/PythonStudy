import pymysql
connect = pymysql.Connect(
  host='192.168.0.103',
  port=3307,
  user='root',
  passwd='123456',
  db='mysql',
  charset='utf8'
)
print(connect)