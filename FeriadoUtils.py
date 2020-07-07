from datetime import datetime, timedelta

class FeriadoUtils:

    utils = None
    ano_corrente = ''
    current_data = ''
    prefixos = []
    nacionais_moveis = {}

    def __init__(self, utils):
        self.utils = utils

        self.resetAnoCorrente()
        self.prefixos = ['12','27','16','13','29','23','53','32','52','21','51','50','31','15','25','41','26','22','33','24','43','11','14','42','35','28','17']

        self.nacionais_moveis['pascoa'] = {'nome':'Páscoa'}
        self.nacionais_moveis['carnaval'] = {'diferenca':-47, 'nome':'Carnaval'}
        self.nacionais_moveis['sexta-feira-santa'] = {'diferenca':-2, 'nome':'Sexta-Feira Santa'}
        self.nacionais_moveis['corpus-christi'] = {'diferenca':60, 'nome':'Corpus Christi'}

        self.calculaDiasFeriadoMovel(self.ano_corrente)

    def resetAnoCorrente(self):
        self.ano_corrente = self.getCurTime('Y')

    def calculaDiasFeriadoMovel(self, ano):
        self.nacionais_moveis['pascoa']['dia'] = self.calculaPascoa( ano )
        for nome in self.nacionais_moveis:
            if nome != 'pascoa':
                self.nacionais_moveis[nome]['dia'] = self.calculaDiaFeriadoMovel(self.nacionais_moveis[nome]['diferenca'])

    def calculaPascoa(self, ano):
        ano = int(ano)
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

    def isUf(self, l):
        return l in self.prefixos

    def isFeriadoNacionalMovel(self, d):
        return d in self.nacionais_moveis

    def testFeriadosFuturos(self, d):
        data = self.trataData(d)

        self.calculaDiasFeriadoMovel(int(data[0]))
        self.resetAnoCorrente()

        for nome in self.nacionais_moveis:
            if self.nacionais_moveis[nome]['dia'] == d:
                return self.nacionais_moveis[nome]

        return False

    def trataData(self, d):

        d = d.split('-')

        ano = str(d[0] if len(d[0]) == 4 else self.ano_corrente)
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

        # Nacionais fixos e móveis
        # Estaduais
        # Municipais

        aux = self.trataData(data)
        data = self.utils.impode(aux, '-', False)

        self.where = " ( (ano IS NULL AND concat('"+aux[0]+"', '-', mes, '-', dia) = '"+data+"') OR concat(ano, '-', mes, '-', dia) = '"+data+"' ) "

        estado = local if self.isUf(local) else local[0:2]

        if self.isUf(local):
            self.adicional = " AND ( local = '"+estado+"' OR (local IS NULL AND poder = 'N') ) "
        else:
            self.adicional = " AND ( local = '"+local+"' OR local = '"+estado+"' OR (local IS NULL AND poder = 'N') ) "

        return db.select('tb_feriado', [col], self.where, self.adicional)