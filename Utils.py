from datetime import datetime
from flask import abort

class Utils:

    def impode(self, s, char, quotes):
        return (char.join("'{0}'".format(i) for i in s)) if quotes else char.join(s)

    def validRequest(self, request):
        if not request.json:
            abort(400)

    def trataPoder(self, l):
        return 'E' if len(l) == 2 else 'M'

    def trataData(self, d):

        d = d.split('-')

        ano = d[0] if len(d[0]) == 4 else self.getCurTime('Y')
        mes = d[0] if len(d[0]) == 2 else d[1]
        dia = d[len(d) - 1]

        return [ano, mes, dia]

    def getCurTime(self, w):
        if w == 'D':
            return datetime.now().day
        elif w == 'M':
            return datetime.now().month
        elif w == 'Y':
            return datetime.now().year