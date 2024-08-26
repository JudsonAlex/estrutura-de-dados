from listaEncadeada import ListaDePacientes, Paciente

judson = Paciente('Judson', 1, "Saudável")
david = Paciente('David', 2, "Nubando")

lista = ListaDePacientes()

lista.adicionar(judson)
lista.adicionar(david)
lista.listar()

