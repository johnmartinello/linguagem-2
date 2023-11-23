from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def consultar_saldo(self):
        pass

