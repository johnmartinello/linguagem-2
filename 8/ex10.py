from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, nome: str):
        self.nome = nome
        self.com_quem = None
        
    @abstractmethod
    def empresta(self):
        pass
    
    @abstractmethod
    def retorna(self):
        pass

class Livro(Item):
    def __init__(self, nome:str):
        super().__init__(nome)
        
    def bloqueia(self):
        self.bloqueado = True
    
    def desbloqueia(self):
        self.bloqueado = False
        
class ItemRestrito(Item):
    def __init__(self, nome:str):
        super().__init__(nome)
        
    def alteraNivel(self, nivel: int):
        self.nivel = nivel
    
    