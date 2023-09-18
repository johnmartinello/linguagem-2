class CadastroEmpregado:
    def __init__(self, nome: str, funcao: str, data_nascimento: str, telefone: str, peso: float, altura: float, salario: float):
        self.nome = nome
        self.idade = 2023 - int(data_nascimento[6:])
        self.funcao = funcao
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.peso = peso
        self.altura = altura
        self.salario = salario

    def mudar_funcao(self, funcao):
        self.funcao = funcao
        return print(f" funcao de {self.nome} modificada para: {self.funcao}!")

    def mudar_salario(self, salario):
        self.salario = peso
        return print(f"salario de {self.nome} modificado para: {self.salario}!")

    def mudar_telefone(self, telefone):
        self.telefone = telefone
        return print(f" telefone de {self.nome} modificado para: {self.telefone}!")

    def mudar_peso(self, peso):
        self.peso = peso
        return print(f"peso de {self.nome} modificado para: {self.peso}!")


empregado = CadastroEmpregado(
    "jonas", "desenvolvedor", "30/03/2004", "9933425", 62.2, 185.0, 1695.00)
print(empregado.idade)
