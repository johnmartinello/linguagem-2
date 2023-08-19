class Lampada:

    def __init__(self, estado, tipo, temperatura, lumens):
        self.estado = estado
        self.tipo = tipo
        self.temperatura = temperatura
        self.lumens = lumens


lampada = Lampada(
    estado=True,
    tipo="LED",
    temperatura=4000,
    lumens=800,
)

