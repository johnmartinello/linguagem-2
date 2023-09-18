class Poupanca:
    def __init__(self, saldo: float):
        self.saldo = saldo

    def depositar(self, valor: float):
        self.saldo += valor
        print("deposito realizado com sucesso")

    def sacar(self, valor: float):
        if (self.saldo - valor >= 0):
            self.saldo -= valor
            print(f"saque de R${valor:.2f} realizado com sucesso")
        else:
            print(f"salo insuficiente para fazer saque de R${valor:.2f}")


class ContaCorrente:
    def __init__(self, saldo: float, ChequeEspecial: float):
        self.saldo = saldo
        self.cheque_especial = ChequeEspecial

    def depositar(self, valor: float):
        self.saldo += valor
        print(f"deposito de R${valor:.2f} realizado com sucesso")

    def sacar(self, valor: float):
        if (self.saldo - valor >= 0):
            self.saldo -= valor
            print(f"saque de R${valor:.2f} realizado com sucesso")
        else:
            if (self.saldo + self.cheque_especial - valor <= 0):
                print(f"saldo insuficiente para fazer saque de R${valor}")
            else:
                diferenca = abs(self.saldo - valor)
                self.saldo = self.saldo - valor
                print(
                    f"saque de R${valor:.2f} realizado com sucesso. Foi utilizado R$ {diferenca:.2f} do cheque especial ")

    def extrato(self):
        print(f"Valor em conta: R$ {self.saldo:.2f}")


class Banco:
    def __init__(self, ):
        self.ContaCorrente = None
        self.Poupanca = None

    def abreConta(self, saldo: float, ChequeEspecial: float):
        self.ContaCorrente = ContaCorrente(saldo, ChequeEspecial)
        print(f"Conta corrente aberta com sucesso")

    def abrePoupanca(self, saldo: float):
        self.Poupanca = Poupanca(saldo)
        print(f"Poupanca aberta com sucesso")

    def falencia(self):
        if (self.ContaCorrente.saldo <= 0 and self.Poupanca.saldo <= 0):
            print("conta esta falida")


banco = Banco()
banco.abreConta(10000, 5000)
banco.abrePoupanca(25000)
banco.ContaCorrente.extrato()
banco.ContaCorrente.sacar(12000)
banco.ContaCorrente.extrato()
banco.ContaCorrente.depositar(2000)
banco.ContaCorrente.extrato()
banco.Poupanca.sacar(25000)
banco.falencia()
