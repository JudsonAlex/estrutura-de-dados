class Paciente:
    def __init__(self, nome,id, estado) -> None:
        self.nome = nome
        self.id = id
        self.estado = estado
        self.next = None

class ListaDePacientes:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def adicionar(self, paciente: Paciente):
        if self.head is None:
            self.head = paciente
        elif self.tail is None:
            self.head.next = paciente
            self.tail = paciente
        else:
            self.tail.next = paciente
            self.tail = paciente

    
    def listar(self):
        atual = self.head

        while atual is not None:
            print(f'Paciente: {atual.nome}')
            atual = atual.next
