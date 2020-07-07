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
                database = 'd2s5lto2hij18t',
                user = 'olmpqxlstufibe',
                password = 'ae9db5deb023cb3598e7138915b4165b32269e44cb62def87f0ced1cd8ec5275',
                host = 'ec2-3-216-129-140.compute-1.amazonaws.com',
                port = '5432', 
                sslmode='require'
            )
            # self.conn = psycopg2.connect(
            #     database = 'colossal',
            #     user = 'postgres',
            #     password = 'root',
            #     host = 'localhost',
            #     port = '5432'
            # )

            # self.engine = create_engine('postgresql+psycopg2://postgres:root@localhost:5432/colossal', echo=True)
            # Session = sessionmaker(bind=engine)
            # self.session = Session()

            self.cur = self.conn.cursor()

        except (Exception, psycopg2.Error) as error :
            print("Falha ao conectar", error)

    def run(self, sql, method):
        try:

            if method == 'select':
                self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
            
            self.cur.execute(sql)

            if method == 'select':
                return self.cur.fetchall()
            elif method == 'do':
                self.conn.commit()

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
            print({'r':'error', 'cause':str(error) })
            self.cur.execute("ROLLBACK")
            self.conn.commit()
            return {'r':'error', 'cause':str(error) }

    def update(self, table, cols, vals, where):
        try:
            self.cur = self.conn.cursor()
            self.sql = " UPDATE " + table + " SET "

            for val in cols:
                self.sql += val + ' = %s, '

            self.sql = self.sql[0:len(self.sql)-2]

            self.sql += " WHERE " + where
            # print(self.sql)
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

            return True

        except (Exception, psycopg2.Error) as error :
            self.cur.execute("ROLLBACK")
            self.conn.commit()
            return {'r':'error', 'cause':str(error) }

    def showSql(self):
        print(self.sql)
        return self

    def close(self):
        self.cur.close()
        self.conn.close()
