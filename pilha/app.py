from pilha_livro import PilhaDeLivros, Livro

livros = [
    Livro('Alice no País das Maravilhas', 224),
    Livro('A Arte da Guerra', 158),
    Livro('1984', 328),
    Livro('O Senhor dos Anéis', 1178),
    Livro('Dom Quixote', 863),
    Livro('O Pequeno Príncipe', 96),
    Livro('Moby Dick', 635),
    Livro('Orgulho e Preconceito', 432),
    Livro('Cem Anos de Solidão', 417),
    
]
pilha = PilhaDeLivros()

for livro in livros:
    pilha.adicionar(livro)

pilha.mostrarTodos()
pilha.remover()
pilha.mostrarTodos()
pilha.exibirTopo()