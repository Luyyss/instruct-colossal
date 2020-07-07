from datetime import datetime, timedelta
from flask import abort

class Utils:

    current_data = ''
    prefixos = []
    nacionais_moveis = {}

    def __init__(self):
        self.prefixos = ['12','27','16','13','29','23','53','32','52','21','51','50','31','15','25','41','26','22','33','24','43','11','14','42','35','28','17']

        self.nacionais_moveis['pascoa'] = {'dia':self.calculaPascoa(), 'nome':'Páscoa'}
        self.nacionais_moveis['carnaval'] = {'dia':self.calculaDiaFeriadoMovel(-47), 'nome':'Carnaval'}
        self.nacionais_moveis['sexta-feira-santa'] = {'dia':self.calculaDiaFeriadoMovel(-2), 'nome':'Sexta-Feira Santa'}
        self.nacionais_moveis['corpus-christi'] = {'dia':self.calculaDiaFeriadoMovel(60), 'nome':'Corpus Christi'}

    def impode(self, s, char, quotes):
        return char.join("'{0}'".format(i) for i in s) if quotes else char.join(s)

    def isUf(self, l):
        return l in self.prefixos

    def isFeriadoNacionalMovel(self, d):
        return d in self.nacionais_moveis

    def validDate(self, dt):

        # data = utils.trataData(dt)
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
            return 'Formato de data incorreto! deve seguir o padrão YYYY-MM-DD ou MM-DD'

    def validLocal(self, local, db):
        if len(local) == 2 and self.isUf(local):
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

    def validRequest(self, request):
        if not request.json:
            abort(400)

    def trataPoder(self, l):
        return 'E' if self.isUf(l) else 'M'

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
        
    def calculaPascoa(self):
        ano = datetime.now().year
        a=ano%19
        b=int(ano/100)
        c=ano%100
        d=int(b/4)
        e=b%4
        f=int((b+8)/25)
        g=int((b-f+1)/3)
        h=((19*a+b-d-g+15)%30)
        i=int(c/4)
        k=c%4
        L=((32+2*e+2*i-h-k)%7)
        m=int((a+11*h+22*L)/451)
        mes=int((h+L-7*m+114)/31)
        dia=((h+L-7*m+114)%31)+1

        mes = mes if mes > 9 else '0'+str(mes)
        dia = dia if dia > 9 else '0'+str(dia)

        return str(ano) + '-'+str(mes) + '-'+str(dia)

    def calculaDiaFeriadoMovel(self, diferenca):

        data = datetime.strptime( '/'.join("{0}".format(int(i)) for i in (self.nacionais_moveis['pascoa']['dia'].split('-')) )  , '%Y/%m/%d')
        data = data + timedelta(days=diferenca)

        mes = data.month
        dia = data.day
        mes = mes if mes > 9 else '0'+str(mes)
        dia = dia if dia > 9 else '0'+str(dia)

        return str(data.year) + '-' + str(mes) + '-' + str(dia)

    def goSearch(self, db, local, data, col):

        ano = str(self.getCurTime('Y'))

        # Nacionais fixos
        # Nacionais móveis
        # Estaduais/Municipais

        data = self.impode(self.trataData(data), '-', False)

        self.where = " ( (ano IS NULL AND concat('"+ano+"', '-', mes, '-', dia) = '"+data+"') OR concat(ano, '-', mes, '-', dia) = '"+data+"' ) "

        estado = local if self.isUf(local) else local[0:2]

        if self.isUf(local):
            self.adicional = " AND ( local = '"+estado+"' OR (local IS NULL AND poder = 'N') ) "
            # ((concat(ano,'-', mes, '-', dia) = '"+data+"' OR (concat('"+ano+"', '-', mes, '-', dia) = '"+ano+"-"+data+"' ))

        else:
            self.adicional = " AND ( local = '"+local+"' OR local = '"+estado+"' OR (local IS NULL AND poder = 'N') ) "

        # print(self.where)
        # print(self.adicional)

        return db.select('tb_feriado', [col], self.where, self.adicional)