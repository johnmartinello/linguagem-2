class Pessoa:
    def __init__(self, nome, idade, altura):
        self._nome = nome
        self._idade = idade
        self._altura = altura

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @property
    def altura(self):
        return self._altura

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    @altura.setter
    def altura(self, altura):
        self._altura = altura

    def imprimir_dados(self):
        print(f"nome: {self.nome}")
        print(f"idade: {self.idade}")
        print(f"altura: {self.altura}")


pessoa = Pessoa("Joao lucas", 19, 1.85)
pessoa.imprimir_dados()
pessoa.nome = "Paulo"
pessoa.idade = 273
pessoa.altura = 1.80
pessoa.imprimir_dados()
