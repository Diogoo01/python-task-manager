from menu import mostrar_menu
from utils import limpar_terminal, pausar, pedir_numero
from ficheiros import carregar_tarefas
from tarefas import (
    mostrar_tarefas,
    adicionar_tarefa,
    remover_tarefa,
    concluir_tarefa,
    limpar_tarefas,
    editar_tarefa,
    pesquisar_tarefas,
    filtrar_tarefas,
    ordenar_tarefas,
    mostrar_estatisticas,
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

    elif escolha == 5:
        limpar_tarefas(tarefas)
        pausar()

    elif escolha == 6:
        editar_tarefa(tarefas)
        pausar()

    elif escolha == 7:
        pesquisar_tarefas(tarefas)
        pausar()

    elif escolha == 8:
        filtrar_tarefas(tarefas)
        pausar()

    elif escolha == 9:
        ordenar_tarefas(tarefas)
        pausar()

    elif escolha == 10:
        mostrar_estatisticas(tarefas)
        pausar()

    elif escolha == 0:
        print("A sair...")
        break

    else:
        print("Por favor introduza um numero valido (0-9)")
        pausar()
