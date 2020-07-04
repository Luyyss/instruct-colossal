from DataBase import DataBase
# from classes import Utils

# utils = Utils()
db = DataBase()
db.insert("tb_feriado", ['nome', 'poder', 'mes', 'dia', 'tipo'], ['Tiradentes', 'N', '04', '21', 'F'])
db.insert("tb_feriado", ['nome', 'poder', 'mes', 'dia', 'tipo'], ['Dia do Trabalhador', 'N', '05', '01', 'F'])
db.insert("tb_feriado", ['nome', 'poder', 'mes', 'dia', 'tipo'], ['Independência', 'N', '09', '07', 'F'])
db.insert("tb_feriado", ['nome', 'poder', 'mes', 'dia', 'tipo'], ['Nossa Senhora Aparecida', 'N', '10', '12', 'F'])
db.insert("tb_feriado", ['nome', 'poder', 'mes', 'dia', 'tipo'], ['Finados', 'N', '11', '02', 'F'])
db.insert("tb_feriado", ['nome', 'poder', 'mes', 'dia', 'tipo'], ['Proclamação da República', 'N', '11', '15', 'F'])
db.insert("tb_feriado", ['nome', 'poder', 'mes', 'dia', 'tipo'], ['Natal', 'N', '12', '25', 'F'])
# db.delete('tb_feriado', 'id_feriado = 8').showSql().do()