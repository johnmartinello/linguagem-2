class Agenda:
    def __init__(self):
        self.pessoas = []

    def armazenar_pessoa(self, nome, numero):
        if len(self.pessoas) > 9:
            print("Limite da agenda alcançado")
        else:
            self.nome = nome
            self.numero = numero
            self.pessoas.append([self.nome, self.numero])

    def buscar_pessoa(self, nome):
        for index, pessoa in enumerate(self.pessoas):
            if pessoa[0] == nome:
                print(f"{nome} esta na posicao {index + 1} da agenda")
                return
        print(f"{nome} nao foi encontrado")

    def imprime_agenda(self):
        for pessoa in self.pessoas:
            print(f"Nome: {pessoa[0]}, Numero: {pessoa[1]}")

    def imprime_pessoa(self, numero: int):
        pessoa = self.pessoas[numero-1]
        print(f"Nome: {pessoa[0]}, Numero: {pessoa[1]} (posicao {numero})")


agenda = Agenda()
agenda.armazenar_pessoa("joao lucas", 123123)
agenda.armazenar_pessoa("roberto", 121212)
agenda.armazenar_pessoa("carlos", 99999)
agenda.armazenar_pessoa("alice", 88888)
agenda.armazenar_pessoa("julia", 77777)
agenda.armazenar_pessoa("giovanna", 666666)
agenda.armazenar_pessoa("ronaldo", 555555)
agenda.armazenar_pessoa("claudio", 444444)
agenda.armazenar_pessoa("robson", 222222)
agenda.armazenar_pessoa("paulo", 111111)


agenda.buscar_pessoa("claudio")
agenda.imprime_agenda()
agenda.imprime_pessoa(5)
