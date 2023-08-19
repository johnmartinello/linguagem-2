class Professor:
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina


professor = Professor("Ober", "Linguagem II")
print(professor.nome)
print(professor.disciplina)
