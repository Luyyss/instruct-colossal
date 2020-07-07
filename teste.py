from DataBase import DataBase
from Utils import Utils

utils = Utils()
db = DataBase()

local = '1600501'
# data = '2020-05-01'
data = 'corpus-christi'
# local = '33'
# data = '11-20'

print(utils.validLocal(local, db))

# data = utils.trataData(data)
poder = utils.trataPoder(local)

# isFeriadoMovel = utils.isFeriadoNacionalMovel(data)

# index_feriados = ''
# if isFeriadoMovel:
#     index_feriados = data
#     data = utils.nacionais_moveis[data]['dia']

# result = utils.goSearch(db, local, data, '*')
# # print(result)

# if len(result) != 0:
#     if poder == 'M' and result[0]['poder'] == 'M':
#         print('Não é permitido cadastrar mais de um feriado para o município no mesmo dia!')

# print(utils.validDate(data))

# print(utils.prefixos)
# print(utils.isUf(local))
# print(utils.trataPoder(local))



# resp = db.delete('tb_feriado', 'id = '+str(result[0]['id']))

# print(resp)

# name = 'teste fer'
# resp = db.update('tb_feriado', ['name'], (str(name), result[0]['id']), 'id = %s' )

# print(db.sql)

# data = 'pascoa'

# print( utils.isFeriadoNacionalMovel(data) )
# print( utils.nacionais_moveis[data]['dia'] )
# print( utils.calculaDiaFeriadoMovel(f) )
# print( utils.moveis )


# db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'tipo'], ['Ano novo', 'N', '01', '01', 'F'])
# db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'tipo'], ['Tiradentes', 'N', '04', '21', 'F'])
# db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'tipo'], ['Dia do Trabalhador', 'N', '05', '01', 'F'])
# db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'tipo'], ['Independência', 'N', '09', '07', 'F'])
# db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'tipo'], ['Nossa Senhora Aparecida', 'N', '10', '12', 'F'])
# db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'tipo'], ['Finados', 'N', '11', '02', 'F'])
# db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'tipo'], ['Proclamação da República', 'N', '11', '15', 'F'])
# db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'tipo'], ['Natal', 'N', '12', '25', 'F'])
# db.delete('tb_feriado', 'id = 8').showSql().do()