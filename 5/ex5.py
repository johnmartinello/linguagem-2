class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.pai = None
        self.mae = None

    def pais(self, pai, mae):
        self.pai = pai
        self.mae = mae

    def mostrar_familia(self, nivel=0):
        espaco = "      " * nivel
        print(f"{espaco}Nome: {self.nome}, Idade: {self.idade}")
        if self.pai:
            print(f"{espaco}Pai:")
            self.pai.mostrar_familia(nivel + 1)
        if self.mae:
            print(f"{espaco}Mãe:")
            self.mae.mostrar_familia(nivel + 1)


filho = Pessoa("Jonas", 19)
pai = Pessoa("Ober", 48)
mae = Pessoa("Carla", 42)
avo_mae = Pessoa("Lucas", 76)
avoh_mae = Pessoa("Mara", 79)
avo_pai = Pessoa("Oro", 76)
avoh_pai = Pessoa("Inelda", 79)
filho.pais(pai, mae)
mae.pais(avo_mae, avoh_mae)
pai.pais(avo_pai, avoh_pai)

filho.mostrar_familia()
