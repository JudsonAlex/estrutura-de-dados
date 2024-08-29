from arvore_binaria import ArvoreBinaria
from random import randint

arvore = ArvoreBinaria()

valores = [randint(0,99) for i in range(10)]
print(valores)

for i in valores:
    arvore.inserir(i)

arvore.percorrer_pos_ordem()