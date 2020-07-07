from datetime import datetime, timedelta
from flask import abort

class Utils:

    # def __init__(self):

    def impode(self, s, char, quotes):
        return char.join("'{0}'".format(i) for i in s) if quotes else char.join(s)

    def validLocal(self, local, db, util):
        if len(local) == 2 and util.isUf(local):
            return True
        elif len(local) == 7:
            qr = db.select('tb_cidade', ['1'], "codigo = '"+local+"'", None)
            if len(qr) != 0:
                return True

        return {'error':'Local incorreto. Deve conter 2 ou 7 caracteres e ser um código válido para cidade ou prefixo conforme IBGE!'}

    def validNumber(self, n, mim, mx, siz, label):
        
        if len(str(n)) != siz:
            return label + ' não tem o tamanho correto ( '+str(siz)+' caracteres )'

        n = int(n)
        if n < mim or n > mx:
            return label + ' não está dentro dos valores permitidos ( '+str(  mim if mim > 9 else '0'+str(mim) )+' até '+str(mx)+' )'

        return True

    def validDate(self, dt):

        d = (dt).split('-')

        if len(d[0]) == 4 or len(d[0]) == 2:

            ano = str(d[0] if len(d[0]) == 4 else '')
            mes = d[0] if len(d[0]) == 2 else d[1]
            dia = d[len(d) - 1]

            if ano != '':
                if len(ano) != 4:
                    return 'Ano deve ser composto por 4 dígitos!'

            resp = self.validNumber(mes, 1, 12, 2, 'Mês')
            if resp != True:
                return resp

            resp = self.validNumber(dia, 1, 31, 2, 'Dia')
            if resp != True:
                return resp

            return True

        else:
            return 'Formato de data incorreto! Deverá seguir o padrão YYYY-MM-DD ou MM-DD'

    def validRequest(self, request):
        if not request.json:
            abort(400)

    def trataPoder(self, l, util):
        return 'E' if util.isUf(l) else 'M'
