import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from Utils import Utils

# engine = create_engine('sqlite:///:memory:', echo=True)
utils = Utils()

class DataBase:

    sql = ''

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                database = 'dcbcf4l61o8l2n',
                user = 'jjsnpzvghssord',
                password = '989264f977fd75081cfd4f7d619f531f5c20120a71ad28b513baffe40172326a',
                host = 'ec2-3-208-50-226.compute-1.amazonaws.com',
                port = '5432', 
                sslmode='require'
            )
            # self.conn = 
            # engine = create_engine('postgresql+psycopg2://postgres:passwordroot:5432/colossal', echo=True)
            # engine = create_engine('postgresql+psycopg2://jjsnpzvghssord:989264f977fd75081cfd4f7d619f531f5c20120a71ad28b513baffe40172326a@ec2-3-208-50-226.compute-1.amazonaws.com:5432/dcbcf4l61o8l2n', echo=True)

            # Session = sessionmaker(bind=engine)
            # self.session = Session()

            self.cur = self.conn.cursor()

        except (Exception, psycopg2.Error) as error :
            print("Falha ao conectar", error)

    def run(self, sql, method):
        try:
            self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
            self.cur.execute(sql)

            if method == 'select':
                return self.cur.fetchall()

        except (Exception, psycopg2.Error) as error :
            print("Falha ao executar", error)

    def select(self, table, cols, where, more):
        try:
            self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
            self.sql = 'SELECT ' + utils.impode(cols, ', ', False) + ' FROM ' + table

            if where is not None:
                self.sql += ' WHERE '+ where

            if more is not None:
                self.sql += ' ' + more

            self.cur.execute(self.sql)

            return self.cur.fetchall()

        except (Exception, psycopg2.Error) as error :
            print("Falha ao buscar", error)

    def insert(self, table, cols, vals):
        try:
            self.cur = self.conn.cursor()
            self.sql = """ INSERT INTO """
            self.sql += table
            self.sql += """ ("""
            self.sql += utils.impode(cols, ', ', False)
            self.sql += """) VALUES ("""

            for i in vals:
                self.sql += '%s, '

            self.sql = self.sql[0:len(self.sql)-2]
            self.sql += """)"""

            self.cur.execute(self.sql, vals)
            self.conn.commit()

            return True

        except (Exception, psycopg2.Error) as error :
            self.cur.execute("ROLLBACK")
            self.conn.commit()
            return {'r':'error', 'cause':str(error) }

    def delete(self, table, where):
        try:
            self.cur = self.conn.cursor()
            self.sql = 'DELETE FROM ' + table + ' WHERE ' + where
            self.cur.execute(self.sql)
            self.conn.commit()

            return self

        except (Exception, psycopg2.Error) as error :
            print("Falha ao deletar", error)

    def showSql(self):
        print(self.sql)
        return self

    def close(self):
        self.cur.close()
        self.conn.close()
