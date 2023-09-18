class CarrodeCorrida:
    def __init__(self, numeroCarro: int, piloto: str, equipe: str, velocidadeMaxima: float):
        self.numeroCarro = numeroCarro
        self.piloto = piloto
        self.equipe = equipe
        self.velocidadeMaxima = velocidadeMaxima
        self.velocidadeAtual = 0
        self.ligado = False

    def get_numero_carro(self):
        return self.numeroCarro

    def get_piloto(self):
        return self.piloto

    def get_equipe(self):
        return self.equipe

    def get_velocidade_maxima(self):
        return self.velocidadeMaxima

    def get_velocidade_atual(self):
        return self.velocidadeAtual

    def get_ligado(self):
        return self.ligado

    def set_numero_carro(self, numeroCarro: int):
        self.numeroCarro = numeroCarro

    def set_piloto(self, piloto: str):
        self.piloto = piloto

    def set_equipe(self, equipe: str):
        self.equipe = equipe

    def set_velocidade_maxima(self, velocidadeMaxima: float):
        self.velocidadeMaxima = velocidadeMaxima

    def set_velocidade_atual(self, velocidade: float):
        self.velocidadeAtual = velocidade

    def set_ligado(self, ligado: bool):
        self.ligado = ligado

    def acelerar(self, velocidade: float):
        if self.ligado:
            if (self.velocidadeAtual + velocidade) <= self.velocidadeMaxima:
                self.velocidadeAtual += velocidade
            else:
                print("Velocidade máxima ultrapassada")
        else:
            print("Carro precisa estar ligado")

    def frear(self, porcentagem: float):
        if self.ligado:
            self.velocidadeAtual = self.velocidadeAtual * \
                ((100 - porcentagem) / 100)
        else:
            print("Carro precisa estar ligado")

    def parar(self):
        self.velocidadeAtual = 0

    def ligar(self):
        self.ligado = True

    def desligar(self):
        if self.velocidadeAtual == 0:
            self.ligado = False
        else:
            print("Carro precisa estar parado para desligar")


carro = CarrodeCorrida(123, "Jonas", "Red Bull", 250)
print(f"piloto: {carro.piloto}. nome da equipe: {carro.equipe}. velocidade maxima: {carro.velocidadeMaxima}")
carro.set_velocidade_maxima(100)
carro.ligar()
carro.acelerar(120)
carro.acelerar(90)
print(f"velocidade atual: {carro.velocidadeAtual}")
carro.frear(10)
print(f"velocidade atual: {carro.velocidadeAtual}")
carro.desligar()
carro.parar()
carro.desligar()
