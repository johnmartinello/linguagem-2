class Televisao:
    def __init__(self):
        self.volume_atual = 0
        self.canal_atual = 0

    def aumentar_volume(self):
        self.volume_atual += 1

    def diminuir_volume(self):
        self.volume_atual -= 1

    def consultar_volume(self):
        print(f"Volume: {self.volume_atual}")

    def aumentar_canal(self):
        self.canal_atual += 1

    def diminuir_canal(self):
        self.canal_atual -= 1

    def definir_canal(self, numero):
        self.canal_atual = numero

    def consultar_canal(self):
        print(f"Canal: {self.canal_atual}")


televisao = Televisao()
televisao.aumentar_canal()
televisao.consultar_canal()
televisao.aumentar_volume()
televisao.consultar_volume()
televisao.definir_canal(23)
televisao.diminuir_volume()
televisao.consultar_canal()
televisao.consultar_volume()
