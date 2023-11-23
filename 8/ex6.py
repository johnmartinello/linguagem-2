from ex4 import Conta
from abc import ABC, abstractmethod


class ContaInvestimento(Conta):
    def __init__(self, numero_conta: str, nome: str, saldo: float):
        super().__init__(numero_conta, nome, saldo)


ci = ContaInvestimento('123-6', 'Maria', 1000.0)
