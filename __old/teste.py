from DataBase import DataBase
from Utils import Utils

utils = Utils()
db = DataBase()

ano = utils.getCurTime('Y')

db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'tipo'], ['Ano novo', 'N', ano, '01', '01', 'F'])
db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'tipo'], ['Tiradentes', 'N', ano, '04', '21', 'F'])
db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'tipo'], ['Dia do Trabalhador', 'N', ano, '05', '01', 'F'])
db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'tipo'], ['Independência', 'N', ano, '09', '07', 'F'])
db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'tipo'], ['Nossa Senhora Aparecida', 'N', ano, '10', '12', 'F'])
db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'tipo'], ['Finados', 'N', ano, '11', '02', 'F'])
db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'tipo'], ['Proclamação da República', 'N', ano, '11', '15', 'F'])
db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'tipo'], ['Natal', 'N', ano, '12', '25', 'F'])
# db.delete('tb_feriado', 'id_feriado = 8').showSql().do()