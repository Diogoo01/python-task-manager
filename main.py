from menu import mostrar_menu
from utils import limpar_terminal, pausar, pedir_numero
from ficheiros import carregar_tarefas
from tarefas import mostrar_tarefas, adicionar_tarefa, remover_tarefa, concluir_tarefa

tarefas = carregar_tarefas()


while True:

    limpar_terminal()
    mostrar_menu()

    escolha = pedir_numero("Escolha: ")

    if escolha == 1:
        mostrar_tarefas(tarefas)
        pausar()

    elif escolha == 2:
        adicionar_tarefa(tarefas)
        pausar()

    elif escolha == 3:
        concluir_tarefa(tarefas)
        pausar()

    elif escolha == 4:
        remover_tarefa(tarefas)
        pausar()

    elif escolha == 0:
        print("A sair...")
        break

    else:
        print("Por favor introduza um numero valido (0-4)")
        pausar()
