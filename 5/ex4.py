class Pessoa:
    def __init__(self, nome: str, contato: str):
        self.nome = nome
        self.contato = contato


class Livro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
        self.com_quem_esta = None

    def visualizar(self):

        if self.com_quem_esta:
            print(f"{self.titulo} ({self.autor}): esta com {self.com_quem_esta.nome}")
        else:
            print(f"{self.titulo} ({self.autor}): esta na estante")


class Emprestimo:
    def __init__(self, livro, pessoa):
        self.livro = livro
        self.pessoa = pessoa
        livro.com_quem_esta = pessoa

    def devolver(self):
        livro.com_quem_esta = None
        print("livro devolvido")


pessoa = Pessoa("jonas", "12345")
livro = Livro("Solaris", "Stanislaw Lem")
livro2 = Livro("Kafka a beira mar", "Haruki Murakami")
emprestimo = Emprestimo(livro, pessoa)
livro.visualizar()
livro2.visualizar()
emprestimo.devolver()
livro.visualizar()
