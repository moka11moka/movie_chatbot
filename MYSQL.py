from pymysql import *
database = 'movie_all'
user_name = 'root'
password = '794463019'
host = 'localhost'
port = 3306

class MYSQL:
    # def __init__(self,host=None,user=None,pwd=None,db=None):
    def __init__(self):
        self.host = host
        self.user = user_name
        self.pwd = password
        self.db = database
        self.port = port

        self._conn = self.GetConnect()
        if (self._conn):
            self._cur = self._conn.cursor()

    # connect to database
    def GetConnect(self):
        conn = False
        try:
            conn = connect(
                self.host,
                self.user,
                self.pwd,
                self.db,
                port = self.port,
                charset = 'utf8'

            )
        except Exception as err:
            print("connection failed, %s" % err)
        else:
            return conn

    # execute query
    def ExecQuery(self, sql):
        res = ""
        try:
            self._cur.execute(sql)
            res = self._cur.fetchall()
        except Exception as err:
            print("execution failed, %s" % err)
        else:
            return res

    # execute non query command
    def ExecNonQuery(self, sql):
        flag = False
        try:
            self._cur.execute(sql)
            self._conn.commit()
            flag = True
        except Exception as err:
            flag = False
            self._conn.rollback()
            print("execution failed, %s" % err)
        else:
            return flag

    # get connection information
    def GetConnectInfo(self):
        print("connection information：")
        print("server:%s , user name:%s , database:%s " % (self.host, self.user, self.db))

    # close connection
    def Close(self):
        if (self._conn):
            try:
                if (type(self._cur) == 'object'):
                    self._cur.close()
                if (type(self._conn) == 'object'):
                    self._conn.close()
            except:
                raise ("close connection failed, %s,%s" % (type(self._cur), type(self._conn)))