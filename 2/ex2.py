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


lampada = LampadaTresEstados()
lampada.estado_atual()
lampada.ligar()
lampada.estado_atual()
lampada.meia_luz()
lampada.estado_atual()
lampada.desligar()
lampada.estado_atual()
