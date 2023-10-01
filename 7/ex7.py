class Animal:
    def __init__(self, nome: str, raca: str):
        self.nome = nome
        self.raca = raca

    def get_animal(self):
        return print(f"{self.nome}: {self.raca}")

    def set_animal(self, nome: str):
        self.nome = nome
        return f"nome mudada para {self.nome}"

    def caminha(self):
        return "caminhando..."


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def late(self):
        return print("auau")


class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def mia(self):
        return print("miau")


cachorro = Cachorro("roberto", "vira-lata")
cachorro.get_animal()
cachorro.late()
gato = Gato("nina", "laranja")
gato.get_animal()
gato.mia()
