class Ingresso:
    def __init__(self, valor: float):
        self.valor = valor

    def imprimeValor(self):
        print(f"Valor do ingresso: R${self.valor:.2f}")


class Vip(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.valor += adicional

    def imprimeValorVip(self):
        print(f"valor do ingresso VIP: R${self.valor:.2f}")


class Normal(Ingresso):
    def __init__(self, valor,):
        super().__init__(valor)

    def tipo(self):
        print(f"ingresso normal")


class CamaroteInferior(Vip):
    def __init__(self, valor, localizacao: str, adicional):
        super().__init__(valor, adicional)
        self.localizacao = localizacao

    def localizar(self):
        print(f"local: {self.localizacao}")


class CamaroteSuperior(Vip):
    def __init__(self, valor, localizacao: str, adicional: float, adicionalVIP: float):
        super().__init__(valor, adicional)
        self.localizacao = localizacao
        self.valor += adicionalVIP

    def localizar(self):
        print(f"local: {self.localizacao}")


ingresso_normal = Normal(50.0)
ingresso_normal.imprimeValor()
ingresso_normal.tipo()

ingresso_vip = Vip(80.0, 30.0)
ingresso_vip.imprimeValor()
ingresso_vip.imprimeValorVip()

camarote_inferior = CamaroteInferior(100.0, "Setor A", 50.0)
camarote_inferior.imprimeValor()
camarote_inferior.imprimeValorVip()
camarote_inferior.localizar()

camarote_superior = CamaroteSuperior(120.0, "Setor B", 60.0, 20.0)
camarote_superior.imprimeValor()
camarote_superior.imprimeValorVip()
camarote_superior.localizar()
