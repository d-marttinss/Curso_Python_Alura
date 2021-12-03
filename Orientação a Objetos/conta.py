
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