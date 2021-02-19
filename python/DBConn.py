import cx_Oracle


class DBConn(object):

    def __init__(self, arg):
        self.CONN_INFO = arg

        conn_str = '{user}/{psw}@{host}:{port}/{service}'.format(**self.CONN_INFO)
        self.conn = cx_Oracle.connect(conn_str, encoding='UTF-8')

    def exec_query(self, gen_query):

        cursor = self.conn.cursor()
        qry_result = cursor.execute(gen_query)
        self.conn.commit()
        cursor.close()
        return qry_result

    def exec_many_query(self, gen_query, data):

        cursor = self.conn.cursor()
        qry_result = cursor.executemany(gen_query, data)
        self.conn.commit()
        cursor.close()
        return qry_result
