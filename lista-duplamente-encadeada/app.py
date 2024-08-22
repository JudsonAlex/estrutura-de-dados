from teste import Produto, ListaDuplamenteEncadeada

produto = Produto('Calça', '123', 15, 12)
produto2 = Produto('furadeira eletrica 220w sigma poewr', '321', 45, 85)
lista = ListaDuplamenteEncadeada()
lista.adicionar(produto)
lista.adicionar(produto2)
lista.listar()
lista.atualizar_estoque('321',8)
lista.remover('123')
lista.listar()
