import pymysql

host = "47.107.168.87"
user = "test"
password = "test"
conn = pymysql.connect(host=host, user=user, password=password,port=3306)
cursor = conn.cursor()
sql = "select Id from future.loan where MemberID=1116521 order by CreateTime desc limit 1"


cursor.execute(sql)
result = cursor.fetchone()[0]
print(result)