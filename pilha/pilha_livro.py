from typing import List

class Livro:
    def __init__(self, titulo, paginas) -> None:
        self.titulo = titulo
        self.n_paginas = paginas


class PilhaDeLivros:
    def __init__(self) -> None:
        self.pilha: List[Livro] = []

    def adicionar(self, livro:Livro):
        self.pilha.append(livro)

    def remover(self):
        removido = self.pilha.pop()
        print(f'[{removido.titulo}] removido')

    def exibirTopo(self):
        print('Topo',self.pilha[-1].titulo)

    def mostrarTodos(self):
        for index, item in enumerate(reversed(self.pilha)):
            print(f'{index + 1}  Título: {item.titulo} - Pág.: {item.n_paginas}')