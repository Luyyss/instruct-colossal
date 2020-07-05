# import json

from flask_restful import Resource, reqparse, request, abort
from DataBase import DataBase
from Utils import Utils

utils = Utils()
db = DataBase()

class FeriadoUtil:

    def goSearch(self, local, data, col):

        # SELECT * FROM tb_feriado 
        # WHERE 
        # ( concat(ano,'-', mes, '-', dia) = '2020-05-01' AND local = 1600501  )
        # OR
        # (ano IS NULL AND concat(mes, '-', dia) = '05-01' AND local IS NULL AND poder = 'N')

        ano = utils.getCurTime('Y')

        return db.select("tb_feriado", [col], 
            " (concat(ano,'-', mes, '-', dia) = '"+data+"' AND local = "+local+" ) " , 
            " OR (ano IS NULL AND concat(mes, '-', dia) = '"+data+"' AND local IS NULL AND poder = 'N' ) " \
            " OR (ano IS NULL AND concat("+ano+", '-', mes, '-', dia) = '"+data+"' AND local IS NULL AND poder = 'N' ) " \
            " LIMIT 1 ")

feriadoUtil = FeriadoUtil()

class FeriadoList(Resource):

    def get(self):

        return db.select("tb_feriado", ['*'], None, None), 200

        # sql = "SELECT tb_cidade.name, " \
        #     "concat(tb_feriado.ano, '-', tb_feriado.mes, '-', tb_feriado.dia) as data, " \
        #     "" \
        #     "FROM tb_feriado JOIN tb_cidade ON tb_feriado.local = tb_cidade.prefixo "

        # return db.run(sql, 'select'), 200


class FeriadoListLocal(Resource):

    def get(self, local):
        return 'ok', 200

class FeriadoListData(Resource):

    def get(self, local, data):

        try:
            result = feriadoUtil.goSearch(local, data, 'name')
            return result[0], 200
        except (Exception) as error:
            return {'error':'Feriado não encontrado'}, 404

    def put(self, local, data):


        try:
            if 'name' not in request.json: #and type(request.json['name']) != unicode
                abort(400)

            self.name = request.json.name
            result = feriadoUtil.goSearch(local, data, '*')

            if result[0]:
                return {'msg':'Cadastro alterado com sucesso'}, 201

            else:
                data = utils.trataData(data)
                poder = utils.trataPoder(local)

                db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'tipo'], [name, poder, data[0], data[1], data[2], 'M'])
                return {'msg':'Cadastro efetuado com sucesso'}, 200

        except (Exception) as error:
            return {'error':'Falha ao salvar feriado'+str(error)}, 500

    def delete(self, local, data):

        try:
            result = feriadoUtil.goSearch(local, data, '*')

            if result[0]['poder'] == 'N':
                return {'error':'Não é permitido deletar feriados nacionais'}, 403

            if result[0]['poder'] == 'E' and (not utils.isUf(local)):
                return {'error':'Não é permitido deletar feriados estaduais pelo munícipio'}, 403

            # return result[0], 200
        except (Exception) as error:
            return {'error':'Feriado não encontrado'}, 404

class Feriado(Resource):

    def get(self, local, data, name):
        return 'ok', 200

    def put(self, local, data):

        utils.validRequest(request)

        name = 'name'
        data = utils.trataData(data)
        poder = utils.trataPoder(local)
        tipo = 'M'

        cols = ['name', 'poder', 'ano', 'mes', 'dia', 'tipo', 'local']
        vals = [name, poder, data[0], data[1], data[2], tipo, local]

        db.insert("tb_feriado", cols, vals)

        print(db.showSql())

        return 'ok', 200

    def delete(self, local, data, name):
        return 'ok', 200