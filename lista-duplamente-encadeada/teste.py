#Requisitos
#Lista dupamente encadeada

class Produto:
    def __init__(self, nome, codigo,preço, quantidade) -> None:
        self.nome = nome
        self.codigo = codigo
        self.preco = preço
        self.quantidade =quantidade

        self.anterior = None
        self.prox = None

class ListaDuplamenteEncadeada:
    def __init__(self) -> None:
        self.head = None
        self.tail = None


    def adicionar(self, produto: Produto):
        if not self.head:
            self.head = produto
            self.tail = produto
        else:
            produto.anterior = self.tail
            self.tail.prox = produto

    def remover(self):
        pass

    def atualizar(self):
        pass

    def listar(self):
        status = True
        atual = self.head
        while status:
            print(atual.nome)
            if atual.prox:
                atual = atual.prox
            else:
                status = False