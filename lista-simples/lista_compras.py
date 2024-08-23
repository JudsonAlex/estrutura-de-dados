class ListaDeCompras():
    def __init__(self) -> None:
        self.itens = []
        self.quantidades = []

    def adicionar_item(self, item, quantidade):
        self.itens.append(item)
        self.quantidades.append(quantidade)

    def remover_item(self, item):
        try:

            index = self.itens.index(item)
            self.itens.remove(item)
            self.quantidades.pop(index)
        except ValueError:
            print(f'{item} não existe na Lista')

    def listar_itens(self):
        if len(self.itens) == 0:
            print('Lista vazia')
            return
        for i in range(len(self.itens)):
            print(f'{self.itens[i]} => {self.quantidades[i]}')
