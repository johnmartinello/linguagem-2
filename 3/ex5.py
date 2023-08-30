class Carro:
    def __init__(self):
        self.tanque = 0
        self.distancia_total = 0

    def abastecer(self, quantia):
        if quantia + self.tanque < 50:
            self.tanque = quantia

    def mover_carro(self, distancia):
        self.distancia_total += distancia
        self.tanque = round(self.tanque - (distancia/15), 2)

    def imprimir_distancia_total(self):
        print(f"distancia total percorrida: {self.distancia_total}")

    def imprimir_tanque(self):
        print(f"tanque restante: {self.tanque}")


carro1 = Carro()
carro1.abastecer(20)
carro2 = Carro()
carro2.abastecer(30)
carro1.mover_carro(200)
carro2.mover_carro(400)
carro1.imprimir_distancia_total()
carro1.imprimir_tanque()
carro2.imprimir_distancia_total()
carro2.imprimir_tanque()
