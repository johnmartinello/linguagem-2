class Produto:
    def __init__(self, preco: float, tamanho: int):
        self.preco = preco
        self.tamanho = tamanho
        self.esta_vendido = False

    def vendido(self):
        self.vendido = True
        return print(f"produto vendido!")


class Venda:
    def __init__(self, comprador, vendedor, produto):
        self.comprador = comprador
        self.vendedor = vendedor
        self.produto = produto

    def concretizaVenda(self):
        if self.comprador.verba >= self.produto.preco:
            self.produto.vendido()
            print("Venda concretizada")
        else:
            print("comprador nao tem dinheiro suficiente para comprar esse produto")

    def cancelaVenda(self):
        self.produto.vendido = False
        print("venda cancelada")


class Vendedor:
    def __init__(self, comissao: float):
        self.comissao = comissao


class Comprador:
    def __init__(self, verba: float):
        self.verba = verba


produto = Produto(10.5, 10)
vendedor = Vendedor(11)
comprador = Comprador(11)
venda = Venda(comprador, vendedor, produto)
venda.concretizaVenda()
venda.cancelaVenda()
