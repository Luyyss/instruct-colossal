import os
from flask import Flask, make_response, jsonify, request
from config import Config, DevelopmentConfig
from Utils import Utils
from flask_sqlalchemy import SQLAlchemy

from DataBase import DataBase

config = Config()
db = DataBase()
utils = Utils()

headers = {"Content-Type": "application/json"}

# print(os.environ['APP_SETTINGS'])

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object(DevelopmentConfig())

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

from models import Estado


@app.route('/')
def hello():
    return "Colossal Company!"

@app.route('/feriados/')
def start():
    return jsonify(db.select('tb_feriado', ['*'], None, None)), 200


@app.route('/limpar/')
def clear():
    db.delete('tb_feriado', 'id > 8')
    return 'ok', 200

@app.route('/feriados/<local>/<data>/', methods=['GET', 'PUT', 'DELETE'])
def defData(local, data):

    isFeriadoMovel = utils.isFeriadoNacionalMovel(data)

    index_feriados = ''
    if isFeriadoMovel:
        index_feriados = data
        data = utils.nacionais_moveis[data]['dia']
    else:
        valid = utils.validDate(data)
        if valid != True:
            return {'error':valid}, 400

    testLocal = utils.validLocal(local, db)
    if testLocal != True:
            return testLocal, 400

    result = utils.goSearch(db, local, data, '*')

    if request.method == 'DELETE':
        if len(result) != 0:
            if result[0]['poder'] == 'N':
                return {'error':'Impossível deletar feriados nacionais'}, 403

            isUf = utils.isUf(local)

            if result[0]['poder'] == 'E' and not isUf:
                return {'error':'Impossível deletar feriados estaduais pelo município'}, 403

            resp = db.delete('tb_feriado', 'id = '+str(result[0]['id']))
            if resp == True:
                return 'ok', 204

            return {'error':'Falha ao deletar feriado'}, 400

        else:
            return {'error':'Feriado não encontrado: '}, 404

    if request.method == 'PUT':

        req = request.get_json()
        name = utils.nacionais_moveis[index_feriados]['nome'] if isFeriadoMovel else req['name']

        try:

            data = utils.trataData(data)
            poder = utils.trataPoder(local)

            if len(result) != 0:
                resp = db.update('tb_feriado', ['name'], (str(name), result[0]['id']), 'id = %s' )
                if resp == True:
                    return {'msg':'Cadastro alterado com sucesso'}, 201

            else:
                resp = db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'local', 'tipo'], (str(name), poder, data[0], data[1], data[2], local, 'M'))

                if resp == True:
                    return {'msg':'Cadastro efetuado com sucesso'}, 200

            return {'error':'Falha ao salvar feriado'}, 400

        except (Exception) as error:
            return {'error':'Falha ao salvar feriado'}, 400 #  +str(error)+", SQL: "+db.sql

        # return jsonify({'met':'put', 'result':result, 'data':data, 'name':name}), 200

    else:
        try:
            result = utils.goSearch(db, local, data, 'name')
            if len(result) != 0:
                return jsonify(result[0]), 200
            else:
                return {'error':'Feriado não encontrado'}, 404

        except (Exception) as error:
            return {'error':'Feriado não encontrado: '}, 404

@app.route('/start_db/')
def startDb():

    db.insert("tb_feriado", ['name', 'poder', 'mes', 'dia', 'tipo'], ['Ano novo', 'N', '01', '01', 'F'])
    db.insert("tb_feriado", ['name', 'poder', 'mes', 'dia', 'tipo'], ['Tiradentes', 'N', '04', '21', 'F'])
    db.insert("tb_feriado", ['name', 'poder', 'mes', 'dia', 'tipo'], ['Dia do Trabalhador', 'N', '05', '01', 'F'])
    db.insert("tb_feriado", ['name', 'poder', 'mes', 'dia', 'tipo'], ['Independência', 'N', '09', '07', 'F'])
    db.insert("tb_feriado", ['name', 'poder', 'mes', 'dia', 'tipo'], ['Nossa Senhora Aparecida', 'N', '10', '12', 'F'])
    db.insert("tb_feriado", ['name', 'poder', 'mes', 'dia', 'tipo'], ['Finados', 'N', '11', '02', 'F'])
    db.insert("tb_feriado", ['name', 'poder', 'mes', 'dia', 'tipo'], ['Proclamação da República', 'N', '11', '15', 'F'])
    db.insert("tb_feriado", ['name', 'poder', 'mes', 'dia', 'tipo'], ['Natal', 'N', '12', '25', 'F'])

    return "ok"

if __name__ == '__main__':
    app.run()