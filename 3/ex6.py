class Elevador:
    def __init__(self, capacidade_total, total_andares):
        self.capacidade_total = capacidade_total
        self.total_andares = total_andares
        self.andar = 0
        self.pessoas_presentes = 0
        
    def entrar(self):
        if self.pessoas_presentes < self.capacidade_total:
            self.pessoas_presentes += 1
        else:
            print("elevador lotado")
    
    def sair(self):
        if self.pessoas_presentes:
            self.pessoas_presentes -= 1
    
    def subir(self):
        if self.andar < self.total_andares:
            self.andar += 1
        else:
            print("elevador ja esta no ultimo andar")
    
    def descer(self):
        if self.andar > 0:
            self.andar -= 1
        else:
            print("elevador ja esta no terreo")
        
    @property
    def capacidade_total(self):
        return self.capacidade_total
    @property
    def total_andares(self):
        return self.total_andares
    @property
    def andar(self):
        return self.andar
    @property
    def pessoas_presentes(self):
        return self.pessoas_presentes