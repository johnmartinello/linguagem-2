class Produto:
    def __init__(self, codigo: str, valor: float, descricao: str):
        self.codigo = codigo
        self.valor = valor
        self.descricao = descricao


class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int):
        self.produto = produto
        self.quantidade = quantidade

class Pedido:
    def __init__(self):
        self.itens = []
        self.valor_total = 0

    def adicionar_item(self, produto: Produto, quantidade: int):
        item = ItemPedido(produto, quantidade)
        self.itens.append(item)

    def obter_total(self):
        self.valor_total = 0
        for item in self.itens:
            self.valor_total += item.produto.valor * item.quantidade

        return self.valor_total


# Exemplo de uso
produto1 = Produto("001", 10.0, "salgadinho")
produto2 = Produto("002", 20.0, "coca 5 litros")

pedido = Pedido()
pedido.adicionar_item(produto1, 3)
pedido.adicionar_item(produto2, 2)

total = pedido.obter_total()
print(f"Total do pedido: R$ {total:.2f}")
