from teste import Produto, ListaDuplamenteEncadeada

produto = Produto('Nub', '123', 15, 12)
produto2 = Produto('jusu', '321', 45, 85)
lista = ListaDuplamenteEncadeada()
lista.adicionar(produto)
lista.adicionar(produto2)
lista.listar()