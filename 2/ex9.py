import math

class Ponto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def valor_escolhido(self):
        return print(f"({self.x}, {self.y})")

    def distancia_reta(self):
        return math.sqrt(self.x**2 + self.y**2)


coordenadas = Ponto2D(6, 10)
coordenadas.valor_escolhido()
print(coordenadas.distancia_reta())
