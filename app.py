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


@app.route('/feriados/<local>/<data>/', methods=['GET', 'PUT', 'DELETE'])
def defData(local, data):

    if request.method == 'PUT':

        req = request.get_json()
        name = req['name']

        try:

            result = utils.goSearch(db, local, data, '*')

            data = utils.trataData(data)
            poder = utils.trataPoder(local)

            if len(result) != 0:

                return {'msg':'Cadastro alterado com sucesso'}, 201

            else:
                resp = db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'tipo'], (str(name), poder, data[0], data[1], data[2], 'M'))

                if(resp == True):
                    return {'msg':'Cadastro efetuado com sucesso'}, 200
                else:
                    return resp.error, 500

        except (Exception) as error:
            return {'error':'Falha ao salvar feriado'+str(error)}, 500

        return jsonify({'met':'put', 'result':result, 'data':data, 'name':name}), 200

    else:
        try:
            result = utils.goSearch(db, local, data, 'name')
            return jsonify(result[0]), 200
            # return db.sql, 200 #[0]
        except (Exception) as error:
            return {'error':'Feriado não encontrado: '+str(error)}, 404


if __name__ == '__main__':
    app.run()