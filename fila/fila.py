from typing import List

class Pedido:
    def __init__(self, numero, cliente, itens, valor) -> None:
        self.numero = numero
        self.cliente = cliente
        self.itens = itens
        self.valor = valor

class FilaDePedidos:
    def __init__(self) -> None:
        self.pedidos: List[Pedido] = []

    def enfileirar(self, pedido: Pedido):
        self.pedidos.append(pedido)

    def desenfileirar(self):
        self.pedidos.pop(0)

    def listar(self):
        print('='*50)
        print(f"{'Numero':^6}|{'Cliente':^13}|{'itens':^23}|{'Valor':^6}")
        print('='*50)
        for pedido in self.pedidos:
            for index, item in enumerate(pedido.itens):
                if index ==0:
                    print(f"{pedido.numero:^6}|{pedido.cliente:^13}|{item:^23}|{pedido.valor:^6}")
                    continue
                
                print('|'.join([" "*6," "*13,f"{item:^23}", " "],))
            print('-'*50)