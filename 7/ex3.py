from ex1 import Carro
from ex2 import Barco


class CarroAnfibio(Carro, Barco):

    def __init__(self, velocidade):
        super().__init__(velocidade)


qual = CarroAnfibio(100)
qual.liga()
