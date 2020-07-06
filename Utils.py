from datetime import datetime
from flask import abort

class Utils:

    prefixos = []

    def __call__(self):
       self.prefixos = [12,27,16,13,29,23,53,32,52,21,51,50,31,15,25,41,26,22,33,24,43,11,14,42,35,28,17]

    def impode(self, s, char, quotes):
        return char.join("'{0}'".format(i) for i in s) if quotes else char.join(s)

    def isUf(self, local):
        return local in self.prefixos

    def validRequest(self, request):
        if not request.json:
            abort(400)

    def trataPoder(self, l):
        return str('E' if self.isUf(l) else 'M')

    def trataData(self, d):

        d = d.split('-')

        ano = str(d[0] if len(d[0]) == 4 else self.getCurTime('Y'))
        mes = str(d[0] if len(d[0]) == 2 else d[1])
        dia = str(d[len(d) - 1])

        return [ano, mes, dia]

    def getCurTime(self, w):
        if w == 'D':
            return str(datetime.now().day)
        elif w == 'M':
            return str(datetime.now().month)
        elif w == 'Y':
            return str(datetime.now().year)
        
    def goSearch(self, db, local, data, col):

        # SELECT * FROM tb_feriado 
        # WHERE 
        # ( concat(ano,'-', mes, '-', dia) = '2020-05-01' AND local = 1600501  )
        # OR
        # (ano IS NULL AND concat(mes, '-', dia) = '05-01' AND local IS NULL AND poder = 'N')

        ano = str(self.getCurTime('Y'))

        return db.select("tb_feriado", [col], 
            " (concat(ano,'-', mes, '-', dia) = '"+data+"' AND local = '"+local+"' ) " , 
            " OR (ano IS NULL AND concat(mes, '-', dia) = '"+data+"' AND local IS NULL AND poder = 'N' ) " \
            " OR (ano IS NULL AND concat('"+ano+"', '-', mes, '-', dia) = '"+data+"' AND local IS NULL AND poder = 'N' ) ")
        #     " LIMIT 1 ")

        # self.where = " concat(ano, '-', mes, '-', dia) = '"+data+"'"

        # self.adicional = " OR concat('"+ano+"', '-', mes, '-', dia) = '"+data+"' " \
        #     " OR (ano IS NULL AND concat(mes, '-', dia) = '"+data+"') "

        # return db.select('tb_feriado', [col], self.where, self.adicional)