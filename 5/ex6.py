class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome
        self.cargo = None
        self.salario = None

    def ver(self):
        print(f"{self.nome}. Cargo: {self.cargo}: R$ {self.salario}")


class Gestao:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, pessoa, cargo: str, salario: float):
        pessoa.cargo = cargo
        pessoa.salario = salario


if __name__ == "__main__":
    pessoa = Pessoa("jonas")
    gestao = Gestao()
    gestao.adicionar_funcionario(pessoa, "desenvolvedor", 1950.50)
    pessoa.ver()
