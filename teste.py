from DataBase import DataBase
from Utils import Utils
from FeriadoUtils import FeriadoUtils

utils = Utils()
feriadoUtil = FeriadoUtils(utils)
db = DataBase()

# local = '1600501'
# data = '2020-05-01'
# data = 'corpus-christi'
# local = '33'
# data = '11-20'

# print(utils.validLocal(local, db))
# print(db.sql)

# data = utils.trataData(data)

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

# db.run("TRUNCATE tb_feriado", 'do')
# # db.run("SELECT pg_catalog.setval(pg_get_serial_sequence('tb_feriado', 'id'), MAX(id)) FROM tb_feriado", 'do')

# db.insert("tb_feriado", ['name', 'poder', 'mes', 'dia', 'tipo'], ['Ano novo', 'N', '01', '01', 'F'])
# db.insert("tb_feriado", ['name', 'poder', 'mes', 'dia', 'tipo'], ['Tiradentes', 'N', '04', '21', 'F'])
# db.insert("tb_feriado", ['name', 'poder', 'mes', 'dia', 'tipo'], ['Dia do Trabalhador', 'N', '05', '01', 'F'])
# db.insert("tb_feriado", ['name', 'poder', 'mes', 'dia', 'tipo'], ['Independência', 'N', '09', '07', 'F'])
# db.insert("tb_feriado", ['name', 'poder', 'mes', 'dia', 'tipo'], ['Nossa Senhora Aparecida', 'N', '10', '12', 'F'])
# db.insert("tb_feriado", ['name', 'poder', 'mes', 'dia', 'tipo'], ['Finados', 'N', '11', '02', 'F'])
# db.insert("tb_feriado", ['name', 'poder', 'mes', 'dia', 'tipo'], ['Proclamação da República', 'N', '11', '15', 'F'])
# db.insert("tb_feriado", ['name', 'poder', 'mes', 'dia', 'tipo'], ['Natal', 'N', '12', '25', 'F'])


print(db.select('tb_feriado', ['*'], ' id IS NOT NULL ', 'LIMIT 10'))

# local = '2111300'
# # data = 'corpus-christi'
# data = '2020-04-10'

# poder = utils.trataPoder(local, feriadoUtil)
# isFeriadoMovel = feriadoUtil.isFeriadoNacionalMovel(data)

# index_feriados = ''
# if isFeriadoMovel:
#     index_feriados = data
#     data = feriadoUtil.nacionais_moveis[data]['dia']
# else:
#     valid = feriadoUtil.validDate(data)
#     if valid != True:
#         print({'error':valid}, 400)

# testLocal = utils.validLocal(local, db, feriadoUtil)
# if testLocal != True:
#         print(testLocal, 400)

# result = feriadoUtil.goSearch(db, local, data, '*')
# print(result, 200)

# try:
#     if len(result) != 0:
#         print({'name':result[0]['name']}, 200)
#     else:

#         # if feriadoUtil.isOutroAno(data):
#         feriado = feriadoUtil.testFeriadosFuturos(data)
#         if feriado != False:
#             data = feriadoUtil.trataData(data)
#             db.insert("tb_feriado", ['name', 'poder', 'ano', 'mes', 'dia', 'local', 'tipo'], (feriado['nome'], poder, data[0], data[1], data[2], local, 'M'))
#             print({'name':feriado['nome']}, 200)
#         # else:



#         print({'error':'Feriado não encontrado 1'}, 404)

# except (Exception) as error:
#     print({'error':'Feriado não encontrado 2'}, 404)
