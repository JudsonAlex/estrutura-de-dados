from no import No

class ArvoreBinaria:
    def __init__(self) -> None:
        self.root = None

    def inserir(self, valor):
        if self.root is None:
            self.root = No(valor)
        else:
            self._inserir(self.root, valor)
    def _inserir(self, no: No, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir(no.esquerda, valor)
        
        else:
            if no.direita is None:
                no.direita = No(valor)

            else:
                self._inserir(no.direita, valor)

    def  percorrer_em_ordem(self):
        self._percorrer_em_ordem(self.root)

    def _percorrer_em_ordem(self, no: No):
        if no is not None:
            self._percorrer_em_ordem(no.esquerda)
            print(no.valor, end=" ")
            self._percorrer_em_ordem(no.direita)

    def  percorrer_pre_ordem(self):
        self._percorrer_pre_ordem(self.root)

    def _percorrer_pre_ordem(self, no: No):
        if no is not None:
            print(no.valor, end=" ")
            self._percorrer_pre_ordem(no.esquerda)
            self._percorrer_pre_ordem(no.direita)

    def  percorrer_pos_ordem(self):
        self._percorrer_pos_ordem(self.root)

    def _percorrer_pos_ordem(self, no:No):
        if no is not None:
            self._percorrer_pos_ordem(no.esquerda)
            self._percorrer_pos_ordem(no.direita)
            print(no.valor, end=" ")

