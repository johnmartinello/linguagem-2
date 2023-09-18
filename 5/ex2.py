class Produto:
    def __init__(self, nome, preco, quantidade_em_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque

    def exibir(self):
        return print(f"{self.nome} - Preço: R${self.preco:.2f} - Estoque: {self.quantidade_em_estoque} unidades")


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = {}
        self.total_pedido = 0  # Renomeado para evitar conflito com o método total()
        self.metodo = None

    def adicionar_item(self, produto, quantidade: int):
        if produto in self.items:
            self.items[produto] += quantidade
        else:
            self.items[produto] = quantidade

        produto.quantidade_em_estoque -= quantidade

    def exibir_pedido(self):
        print(f"Pedido de {self.cliente}:")
        for produto, quantidade in self.items.items():
            print(f"{produto.nome} - Quantidade: {quantidade}")

    def calcular(self):

        self.total_pedido = 0
        for produto, quantidade in self.items.items():
            self.total_pedido += produto.preco * quantidade

    def pagar(self, metodo):
        self.metodo = metodo
        self.calcular()
        print(
            f"Total a ser pago: R$ {self.total_pedido:.2f}. Metodo: {metodo}")


produto = Produto("Miojo", 1, 100)
produto.exibir()
produto2 = Produto("Sucrilhos", 10, 100)

pedido = Pedido("Jonas")
pedido.adicionar_item(produto, 5)
pedido.adicionar_item(produto2, 5)
pedido.exibir_pedido()

pedido.pagar("cartao")
