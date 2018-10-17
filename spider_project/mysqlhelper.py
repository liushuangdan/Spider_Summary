import pymysql

class MysqlHelper(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='projects', charset='utf8mb4')
        self.cursor = self.conn.cursor()

    def execute_modify_sql(self, insert_sql, data):
        self.cursor.execute(insert_sql, data)
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    insert_sql = 'insert into renxing (c1, c2) values(%s, %s)'
    data = (1, "不准任性'")
    helper = MysqlHelper()
    helper.execute_modify_sql(insert_sql, data)