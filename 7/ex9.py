class Imovel:
    def __init__(self, endereco: str, preco: float):
        self.endereco = endereco
        self.preco = preco


class Novo(Imovel):
    def __init__(self, endereco, preco):
        super().__init__(endereco, preco)

    def valor_adicional(self, adicional: float):
        self.adicional = adicional
        self.preco += self.adicional
        print(
            f"Valor adicional de R${self.adicional}. Novo Total: R${self.preco}")

    def get_adicional(self):
        print(f"valor adicional: R${self.adicional:.2f}")


class Velho(Imovel):
    def __init__(self, endereco, preco):
        super().__init__(endereco, preco)

    def valor_menos(self, decrescimo: float):
        self.decrescimo = decrescimo
        self.preco -= self.decrescimo
        print(
            f"Valor a menos de R${self.decrescimo}. Novo Total: R${self.preco}")

    def get_decrescimo(self):
        print(f"valor do decrescimo: R${self.decrescimo:.2f}")


imovel_novo = Novo("Rua A, 123", 100000.0)
imovel_novo.valor_adicional(20000.0)
imovel_novo.get_adicional()

imovel_velho = Velho("Rua B, 456", 80000.0)
imovel_velho.valor_menos(15000.0)
imovel_velho.get_decrescimo()
