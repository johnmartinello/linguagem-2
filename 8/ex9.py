from ex8 import ContaInvestimento
from ex4 import Conta, ContaCorrente, ContaPoupanca
from abc import ABC, abstractmethod

if __name__ == '__main__':
    cc = ContaCorrente('123-4', 'João', 1000.0)
    cp = ContaPoupanca('123-5', 'José', 1000.0)
    ci = ContaInvestimento('123-6', 'Maria', 1000)

    cc.atualiza(0.01)
    cp.atualiza(0.01)
    print(cc.saldo)
    print(cp.saldo)
    ci.atualiza(0.01)
    print(ci.saldo)
