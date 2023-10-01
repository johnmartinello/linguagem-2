class Barco:
    def __init__(self, velocidade):
        self.velocidade = velocidade
        self.ligado = False
        
    def liga(self):
        self.ligado = True
        print("Barco ligado")