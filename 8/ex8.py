from ex4 import Conta
from abc import ABC, abstractmethod


class ContaInvestimento(Conta):
    def __init__(self, numero_conta: str, nome: str, saldo: float):
        super().__init__(numero_conta, nome, saldo)

    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 5


ci = ContaInvestimento('123-6', 'Maria', 1000)
ci.atualiza(0.01)
print(ci.saldo)
