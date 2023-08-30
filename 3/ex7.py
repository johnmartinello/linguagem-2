class Relogio:
    def setHora(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
    
    def getHora(self):
        return self.hora, self.minuto, self.segundo
    
    def avancar_segundo(self):
        self.segundo += 1
        
        if self.segundo == 60:
            self.minuto += 1
            self.segundo = 0
            
        if self.minuto == 60:
            self.hora += 1
            self.minuto = 0