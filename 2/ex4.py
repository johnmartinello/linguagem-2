class LampadaTresEstados:

    def __init__(self):
        self.estado = "apagada"

    def ligar(self):
        self.estado = "acesa"

    def desligar(self):
        self.estado = "apagada"

    def meia_luz(self):
        self.estado = "meia_luz"

    def estado_atual(self):
        return print(self.estado)

    def estaLigada(self):
        if self.estado == "acesa" or self.estado == "meia_luz":
            return True
        else:
            return False


lampada = LampadaTresEstados()
lampada.ligar()
print(lampada.estaLigada())
