class Pedido:
    def __init__(self, numero, cliente, itens, valor) -> None:
        self.numero = numero
        self.cliente = cliente
        self.itens = itens
        self.valor = valor

class FilaDePedidos:
    def __init__(self) -> None:
        self.inicio = None
        self.fim = None

    def enfileirar(self):
        pass

    def desenfileirar(self):
        pass