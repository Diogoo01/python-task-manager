from menu import mostrar_menu
from utils import limpar_terminal, pausar, pedir_numero
from gestor_tarefas import GestorTarefas

gestor = GestorTarefas()


while True:

    limpar_terminal()
    mostrar_menu()

    escolha = pedir_numero("Selecione uma opção: ")

    if escolha == 1:
        gestor.mostrar_tarefas()
        pausar()

    elif escolha == 2:
        gestor.adicionar_tarefa()
        pausar()

    elif escolha == 3:
        gestor.concluir_tarefa()
        pausar()

    elif escolha == 4:
        gestor.remover_tarefa()
        pausar()

    elif escolha == 5:
        gestor.limpar_tarefas()
        pausar()

    elif escolha == 6:
        gestor.editar_tarefa()
        pausar()

    elif escolha == 7:
        gestor.pesquisar_tarefas()
        pausar()

    elif escolha == 8:
        gestor.filtrar_tarefas()
        pausar()

    elif escolha == 9:
        gestor.ordenar_tarefas()
        pausar()

    elif escolha == 10:
        gestor.mostrar_estatisticas()
        pausar()

    elif escolha == 0:
        print("A sair...")
        break

    else:
        print("Por favor introduza um numero valido (0-10)")
        pausar()
