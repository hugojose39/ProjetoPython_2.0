class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposito(self, valor):
        self.__saldo += valor

    def __saldo_disponivel(self, valor_retirado):
        valor_disponivel = self.__saldo + self.__limite
        return valor_retirado <= valor_disponivel

    def saque(self, valor):
        if(self.__saldo_disponivel(valor)):
            self.__saldo -= valor
        else:
            print("Infelizmente o senhor tentou sacar um valor maior que o limite de sua conta")

    def extrato(self):
        print("Saldo de sua conta é R$ {:7.2f}".format(self.__saldo))

    def transfere(self, valor, destino):
        if(self.__saldo_disponivel(valor)):
            self.saque(valor)
            destino.deposito(valor)
        else:
            print("Infelizmente a tranferência não foi efetuada, pois o valor digitado é maior que o limite de sua conta")

    def get_numero(self):
        return self.__numero

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'CAIXA':'104', 'BRADESCO':'237'}
