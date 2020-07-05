import psycopg2
from psycopg2.extras import RealDictCursor
from Utils import Utils
# import numpy as np

utils = Utils()

class DataBase:

    sql = ''

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                database = 'colossal',
                user = 'postgres',
                password = 'root',
                host = 'localhost',
                port = '5432'
            )
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
        # try:
            self.cur = self.conn.cursor()
            self.sql = """ INSERT INTO """
            self.sql += table
            self.sql += """ ("""
            self.sql += utils.impode(cols, ', ', False)
            self.sql += """) VALUES ("""
            self.sql += utils.impode(vals, ', ', True)
            self.sql += """)"""

            self.cur.execute(self.sql)
            self.conn.commit()

        # except (Exception, psycopg2.Error) as error :
        #     print("Falha ao inserir", error)


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
