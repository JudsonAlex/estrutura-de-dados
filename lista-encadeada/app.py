class Paciente:
    def __init__(self, nome,id, estado) -> None:
        self.nome = nome
        self.id = id
        self.estado = estado

class ListaDePacientes:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def adicionar(self, paciente):
        pass
        