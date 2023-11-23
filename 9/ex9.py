class ContaExceção(Exception):
    def __init__(self, message="Saldo negativo na conta"):
        super().__init__(message)


class Conta:
    def __init__(self):
        self.saldo = 0
        self.limite = 0

    def deposita(self, valor):
        self.saldo += valor

    def setLimite(self, limite):
        self.limite = limite

    def saca(self, valor):
        if self.saldo - valor < -self.limite:
            raise ContaExceção()
        self.saldo -= valor


try:
    minhaConta = Conta()
    minhaConta.deposita(150)
    minhaConta.setLimite(200)
    minhaConta.saca(500)
    print("Operação concluída com sucesso. Saldo atual:", minhaConta.saldo)

except ContaExceção as e:
    print("Erro:", str(e))
