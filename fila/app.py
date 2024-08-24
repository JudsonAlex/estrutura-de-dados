from fila import FilaDePedidos, Pedido

p1 = Pedido(1,'Judson', ['cabeça', 'ombro', 'joelho', 'pé'], 100)
p2 = Pedido(2,'Petter', ['Olhos', 'ouvido', 'Boca', 'Nariz'], 20)

l_pedidos = FilaDePedidos()
l_pedidos.enfileirar(p1)
l_pedidos.enfileirar(p2)

l_pedidos.listar()
l_pedidos.desenfileirar()
l_pedidos.listar()

