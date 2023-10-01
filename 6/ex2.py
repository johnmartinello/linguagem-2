from ex1 import Pessoa


class Fornecedor(Pessoa):
    def __init__(self, nome: str, endereco: str, credimaximo: float, valorEmDivida: float):
        super().__init__(nome, endereco)
        self.credimaximo = credimaximo
        self.valorEmDivida = valorEmDivida

    def get_credimaximo(self):
        return self.credimaximo

    def set_credimaximo(self, novo_credimaximo: str):
        self.credimaximo = novo_credimaximo
        return print(f"credimaximo mudado para '{self.credimaximo}'")

    def get_valorEmDivida(self):
        return self.valorEmDivida

    def set_valorEmDivida(self, novo_valorEmDivida: str):
        self.valorEmDivida = novo_valorEmDivida
        return print(f"valorEmDivida mudado para '{self.valorEmDivida}'")

    def obterSaldo(self):
        return print(f"saldo: {self.credimaximo-self.valorEmDivida}")


fornecedor = Fornecedor("jonas", "rua pindamangueira 3343", 2000, 1500)
print(fornecedor.get_nome())
print(fornecedor.get_endereco())
print(fornecedor.get_credimaximo())
print(fornecedor.get_valorEmDivida())
fornecedor.obterSaldo()
fornecedor.set_nome("roberto")
fornecedor.set_endereco("alela")
fornecedor.set_credimaximo(2500)
fornecedor.set_valorEmDivida(1500)
fornecedor.obterSaldo()
