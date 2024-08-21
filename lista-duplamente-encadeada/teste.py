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

    
    def remover(self, codigo):
        atual = self.head
        while atual:
            if atual.codigo == codigo:
                if atual.anterior is None and atual.prox is None:
                    self.head = None
                    self.tail = None
                elif atual.anterior is None:
                    self.head = atual.prox
                    self.head.anterior = None

                elif atual.prox is None:
                    self.tail = atual.anterior
                    self.tail.prox = None

                else:
                    atual.anterior.prox = atual.prox
                    atual.prox.anterior = atual.anterior

                print(f"{atual.nome} - [Removido]")
                atual.anterior = None
                atual.prox = None
                return
            else:
                atual = atual.prox


            


    def atualizar_estoque(self, codigo, valor):
        atual = self.head
        while atual:
            if atual.codigo == codigo:
                atual.quantidade = valor
                return
            atual = atual.prox
            

    def listar(self):
        status = True
        atual = self.head
        while status:
            print(atual.nome)
            if atual.prox:
                atual = atual.prox
            else:
                status = False