class Pessoa:
    def __init__(self, nome: str, endereco: str):
        self.nome = nome
        self.endereco = endereco

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome: str):
        self.nome = novo_nome
        print(f"Nome mudado para '{self.nome}'")

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, novoendereco: str):
        self.endereco = novoendereco
        print(f"Endereço mudado para '{self.endereco}'")
