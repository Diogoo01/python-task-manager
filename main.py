from menu import mostrar_menu
from utils import limpar_terminal, pausar, pedir_numero
from ficheiros import carregar_tarefas
from tarefas import (
    mostrar_tarefas,
    adicionar_tarefa,
    remover_tarefa,
    concluir_tarefa,
    limpar_tarefas,
)

tarefas = carregar_tarefas()


while True:

    limpar_terminal()
    mostrar_menu()

    escolha = pedir_numero("Selecione uma opção: ")

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

    elif escolha == 5:
        limpar_tarefas(tarefas)
        pausar()

    else:
        print("Por favor introduza um numero valido (0-4)")
        pausar()
