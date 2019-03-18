import pymysql

class MysqlUtil:
    def __init__(self):
        host = "47.107.168.87"
        user = "test"
        password = "test"
        #1.建立连接
        self.conn = pymysql.connect(host=host, user=user, password=password,port=3306)
        # 2.新建一个查询页面
        self.cursor = self.conn.cursor()
    def fetchone(self,sql):
        # 4.执行SQL
        self.cursor.execute(sql)
        # 5.查看结果
        result = self.cursor.fetchone()
        return result
    def close(self):
        self.cursor.close()
        self.conn.close()
if __name__ == '__main__':
    mysql = MysqlUtil()
    # sql = "select max(mobilephone) from future.member"
    sql = "select * from future.member where mobilephone=18800000001"
    result = mysql.fetchone(sql)
    print(result)