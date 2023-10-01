class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade


class Rica(Pessoa):
    def __init__(self, nome, idade, dinheiro):
        super().__init__(nome, idade)
        self.dinheiro = dinheiro

    def fazCompras(self, gasto: float):
        self.dinheiro -= gasto
        print(f"gastou R${gasto}. Dinheiro restante: R${self.dinheiro:.2f}")


class Pobre(Pessoa):
    def __init__(self, nome, idade, cargo: str):
        super().__init__(nome, idade)
        self.cargo = cargo

    def trabalha(self):
        print("trabalhando...")


class Miseravel(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def mendiga(self):
        print("mendigando...")


pessoa_rica = Rica("Carlos", 30, 10000.0)
pessoa_pobre = Pobre("Maria", 25, "caixa")
pessoa_miseravel = Miseravel("João", 40)

print("Pessoa Rica:")
print(f"Nome: {pessoa_rica.nome}")
print(f"Idade: {pessoa_rica.idade}")
print(f"Dinheiro: R${pessoa_rica.dinheiro}")
pessoa_rica.fazCompras(500)
print()

print("Pessoa Pobre:")
print(f"Nome: {pessoa_pobre.nome}")
print(f"Idade: {pessoa_pobre.idade}")
print(f"Cargo: {pessoa_pobre.cargo}")
pessoa_pobre.trabalha()
print()

print("Pessoa Miserável:")
print(f"Nome: {pessoa_miseravel.nome}")
print(f"Idade: {pessoa_miseravel.idade}")
pessoa_miseravel.mendiga()
