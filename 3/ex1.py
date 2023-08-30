import math


class Circulo:

    def __calcular_area(self):
        self.area = math.pi*(self.raio*self.raio)

    def __calcular_circunferencia(self):
        self.circunferencia = 2 * math.pi * self.raio

    def definir_raio(self, raio):
        self.raio = raio

    def aumentar_raio_porcentagem(self, porcentagem):
        self.raio = self.raio * (1+(porcentagem/100))

    def definir_centro_circulo(self, X, Y):
        self.X = X
        self.Y = Y

    def imprimir_raio(self):
        return print(f"valor do raio: {self.raio}")

    def imprimir_centro_circulo(self):
        return print(f"centro do circulo: ({self.X}, {self.Y})")

    def imprimir_area(self):
        return print(f" valor da area do circulo: {self.area}")


circulo = Circulo()

circulo.definir_raio(10)
circulo.imprimir_raio()

circulo.definir_centro_circulo(10, 5)
circulo.imprimir_centro_circulo()

circulo._Circulo__calcular_area()
print(f"area do circulo: {round(circulo.area, 2)}")

circulo._Circulo__calcular_circunferencia()
print(f"circunferencia: {round(circulo.circunferencia, 2)}")
