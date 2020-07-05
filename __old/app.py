from flask import Flask
from feriado import FeriadoList, FeriadoListLocal, FeriadoListData, Feriado
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(FeriadoList, '/feriados/')
api.add_resource(FeriadoListLocal, '/feriados/<string:local>/')
api.add_resource(FeriadoListData, '/feriados/<string:local>/<string:data>/')
api.add_resource(Feriado, '/feriados/<string:local>/<string:data>/<string:name>/')

app.run(debug=True)