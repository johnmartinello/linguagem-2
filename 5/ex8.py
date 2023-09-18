class Motor:
    def __init__(self, cilindros: int, cavalos: int):
        self.cilindros = cilindros
        self.cavalos = cavalos


class Pneu:
    def __init__(self, marca: str, tipo: str):
        self.marca = marca
        self.tipo = tipo


class Carro:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.pneu = None
        self.motor = None

    def visualizar(self):
        return print(f"{self.marca} {self.modelo}: motor V{self.motor.cilindros}({self.motor.cavalos}). Pneu {self.pneu.marca}: tipo {self.pneu.tipo}")

    def adicionar_motor(self, cilindros: int, cavalos: int):
        motor = Motor(cilindros, cavalos)
        self.motor = motor

    def adicionar_pneu(self, marca: str, tipo: str):
        pneu = Pneu(marca, tipo)
        self.pneu = pneu


carro = Carro("Honda", "Civic 2022")
carro.adicionar_motor(8, 240)
carro.adicionar_pneu("michelin", "duro")
carro.visualizar()
