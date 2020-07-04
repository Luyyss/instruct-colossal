from flask_restful import Resource, reqparse
from DataBase import DataBase
from Utils import Utils

utils = Utils()
db = DataBase()

class FeriadoList(Resource):

    def get(self):

        return db.select("tb_feriado", ['*'], None, None), 200

        # sql = "SELECT tb_cidade.nome, " \
        #     "concat(tb_feriado.ano, '-', tb_feriado.mes, '-', tb_feriado.dia) as data, " \
        #     "" \
        #     "FROM tb_feriado JOIN tb_cidade ON tb_feriado.local = tb_cidade.prefixo "

        # return db.run(sql, 'select'), 200


class FeriadoListLocal(Resource):

    def get(self, local):
        return 'ok', 200

class FeriadoListData(Resource):

    def get(self, local, data):
        return 'ok', 200

    def put(self, local, data):
        return 'ok', 200

    def delete(self, local, data):
        return 'ok', 200

class Feriado(Resource):

    def get(self, local, data, nome):
        return 'ok', 200

    def put(self, local, data, nome):

        data = utils.trataData(data)
        poder = 'E' if len(local) == 2 else 'M'
        tipo = 'M'

        cols = ['nome', 'poder', 'ano', 'mes', 'dia', 'tipo', 'local']
        vals = [nome, poder, data[0], data[1], data[2], tipo, local]

        db.insert("tb_feriado", cols, vals)

        print(db.showSql())

        return 'ok', 200

    def delete(self, local, data, nome):
        return 'ok', 200