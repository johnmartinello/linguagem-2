from ex1 import Pessoa


class Cliente(Pessoa):
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


cliente = Cliente("jonas", "rua pindamangueira 3343", 2000, 1500)
print(cliente.get_nome())
print(cliente.get_endereco())
print(cliente.get_credimaximo())
print(cliente.get_valorEmDivida())
cliente.obterSaldo()
cliente.set_nome("roberto")
cliente.set_endereco("alela")
cliente.set_credimaximo(2500)
cliente.set_valorEmDivida(1500)
cliente.obterSaldo()
