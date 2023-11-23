from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, numero_conta: str, nome: str, saldo: float):
        self.numero_conta = numero_conta
        self.nome = nome
        self.saldo = saldo

    @abstractmethod
    def atualiza(self, saldo):
        pass


class ContaCorrente(Conta):
    def __init__(self, numero_conta: str, nome: str, saldo: float):
        super().__init__(numero_conta, nome, saldo)

    def atualiza(self, saldo):
        self.saldo = saldo
        return self.saldo


class ContaPoupanca(Conta):
    def __init__(self, numero_conta: str, nome: str, saldo: float):
        super().__init__(numero_conta, nome, saldo)

    def atualiza(self, saldo):
        self.saldo = saldo
        return self.saldo


if __name__ == '__main__':
    cc = ContaCorrente('123-4', 'João', 1000.0)
    cp = ContaPoupanca('123-5', 'José', 1000.0)

    cc.atualiza(0.01)
    cp.atualiza(0.01)
    print(cc.saldo)
    print(cp.saldo)
