from flask import Flask, jsonify, request
from config import ProductionConfig

from Utils import Utils
from FeriadoUtils import FeriadoUtils
from DataBase import DataBase

db = DataBase()
utils = Utils()
feriadoUtil = FeriadoUtils(utils)

headers = {"Content-Type": "application/json"}

app = Flask(__name__)
app.config.from_object(ProductionConfig())

@app.route('/')
def hello():
    return "Hello to Colossal Company!", 200


@app.route('/feriados/')
def start():
    return jsonify(db.select('tb_feriado', ['*'], None, None)), 200


@app.route('/feriados/<local>/<data>/', methods=['GET', 'PUT', 'DELETE'])
def defData(local, data):

    poder = utils.trataPoder(local, feriadoUtil)
    isFeriadoMovel = feriadoUtil.isFeriadoNacionalMovel(data)

    index_feriados = ''
    if isFeriadoMovel:
        index_feriados = data
        data = feriadoUtil.nacionais_moveis[data]['dia']
    else:
        valid = utils.validDate(data)
        if valid != True:
            return {'error':valid}, 400

    testLocal = utils.validLocal(local, db, feriadoUtil)
    if testLocal != True:
            return testLocal, 400

    result = feriadoUtil.goSearch(db, local, data, '*')

    if request.method == 'GET':
        try:
            if len(result) != 0:
                return {'name':result[0]['name']}, 200
            else:

                feriado = feriadoUtil.testFeriadosFuturos(data)
                if feriado != False:
                    data = feriadoUtil.trataData(data)
                    db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'local', 'tipo'], (feriado['nome'], poder, data[0], data[1], data[2], local, 'M'))
                    return {'name':feriado['nome']}, 200

                return {'error':'Feriado não encontrado'}, 404

        except (Exception) as error:
            return {'error':'Feriado não encontrado'}, 404


    elif request.method == 'DELETE':
        if len(result) != 0:
            isUf = feriadoUtil.isUf(local)

            if result[0]['poder'] == 'N':
                return {'error':'Impossível deletar feriados nacionais'}, 403

            if result[0]['poder'] == 'E' and not isUf:
                return {'error':'Impossível deletar feriados estaduais pelo município'}, 403

            resp = db.delete('tb_feriado', 'id = '+str(result[0]['id']))
            if resp == True:
                return 'ok', 204

            return {'error':'Falha ao deletar feriado'}, 400

        else:
            return {'error':'Feriado não encontrado: '}, 404

    elif request.method == 'PUT':

        if isFeriadoMovel:
            name = feriadoUtil.nacionais_moveis[index_feriados]['nome'] 
        else:
            req = request.get_json()
            name = req['name']

        try:
            data = feriadoUtil.trataData(data)

            if len(result) != 0:

                if result[0]['poder'] == 'N':
                    if poder == 'E':
                        return {'error':'Impossível inserir feriado estadual, já existe um feriado nacional'}, 403
                    if poder == 'M':
                        return {'error':'Impossível inserir feriado municipal, já existe um feriado nacional'}, 403

                if result[0]['poder'] == 'E' and poder == 'M':
                    return {'error':'Impossível inserir feriado municipal, já existe um feriado estadual'}, 403

                resp = db.update('tb_feriado', ['name'], (str(name), result[0]['id']), 'id = %s' )
                if resp == True:
                    return {'msg':'Cadastro alterado com sucesso'}, 200

            else:
                resp = db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'local', 'tipo'], (str(name), poder, data[0], data[1], data[2], local, 'M'))

                if resp == True:
                    return {'msg':'Cadastro efetuado com sucesso'}, 201

            return {'error':'Falha ao salvar feriado'}, 400

        except (Exception) as error:
            return {'error':'Falha ao salvar feriado'}, 400


if __name__ == '__main__':
    app.run()