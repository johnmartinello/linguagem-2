class Contato:
    def __init__(self, nome: str, numero: int):
        self.nome = nome.lower()
        self.numero = numero

    def mudar_numero(self, numero):
        self.numero = numero
        return print(f"numero mudado com sucesso para: {numero}")


class Agenda:
    def __init__(self):
        self.lista = {}

    def ver_lista(self):
        print("lista telefonica:")
        for pessoa, numero in self.lista.items():
            print(f"{pessoa}: {numero}")

    def procurar_pessoa(self, pessoa: str):

        if pessoa in self.lista:
            print(f"Pessoa encontrada. Numero: {self.lista.get(pessoa)}")
        else:
            print("pessoa nao encontrada")

    def adicionar(self, contato):
        self.lista[contato.nome] = contato.numero


contato = Contato("JONAS", 999887766)
contato2 = Contato("roberto", 111334455)
agenda = Agenda()
agenda.adicionar(contato)
agenda.adicionar(contato2)

agenda.ver_lista()
agenda.procurar_pessoa("jonas")
agenda.procurar_pessoa("ana")
