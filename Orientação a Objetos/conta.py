
class Conta:

    def __init__(self, numero, nome, saldo, limite):
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo
        self.__limite = limite

        print("Criando conta")

    def extrato(self):
        print(f"saldo de {self.__saldo} do titular {self.__nome}")

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__nome

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite