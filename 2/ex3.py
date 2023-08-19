class LampadaTresEstados:

    def __init__(self):
        self.luminosidade = 0

    def ajustar_iluminacao(self, luminosidade):
        self.luminosidade = luminosidade

    def luminosidade_atual(self):
        return print(self.luminosidade)


lampada = LampadaTresEstados()
lampada.luminosidade_atual()
lampada.ajustar_iluminacao(50)
lampada.luminosidade_atual()
