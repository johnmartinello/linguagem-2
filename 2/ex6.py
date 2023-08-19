class Time:

    def __init__(self, nome, jogadores, campeonato, pontos):
        self.nome = nome
        self.jogadores = jogadores
        self.campeonato = campeonato
        self.pontos = pontos


time = Time(
    nome="barsemlona",
    jogadores=["jonas", "ronaldo", "cleito"],
    campeonato="brasileiro",
    pontos=8
)
print(time.campeonato)
