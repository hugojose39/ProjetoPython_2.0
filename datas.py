class Data:

    def __init__(self, dia, mes , ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprime_data(self):
        print("Data {:02d}/{:02d}/{:4d}".format(self.dia, self.mes, self.ano))