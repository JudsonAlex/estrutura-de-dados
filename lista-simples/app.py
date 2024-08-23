from lista_compras import ListaDeCompras

lista = ListaDeCompras()
isRun = True

while isRun:
    print('escolha a operação:')
    print('1 - Listar\n2 - Adicionar\n3 - Remover')
    escolha = input()

    if 0 > int(escolha) > 3:
        print('valor invalido')
    elif int(escolha) == 1:
        lista.listar_itens()
    elif int(escolha) == 2:
        item = input('digite o nome do item\n')
        quantidade = int(input('digite a quantidade\n'))
        lista.adicionar_item(item, quantidade)
    elif int(escolha) == 3:
        item = input('digite o nome do item a ser removido\n')
        lista.remover_item(item)
    elif int(escolha) == 0:
        isRun =False
    