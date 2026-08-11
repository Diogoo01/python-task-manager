from ficheiros import guardar_tarefas
from utils import pedir_numero


def mostrar_tarefas(tarefas):
    if not tarefas:
        print("Não existem tarefas.")
        return

    for i, tarefa in enumerate(tarefas, start=1):
        estado = "[X]" if tarefa["concluida"] else "[ ]"
        print(i, "-", estado, tarefa["nome"])


def adicionar_tarefa(tarefas):
    tarefa_adicionada = input("Insira o nome da tarefa que pretende adicionar: ")
    tarefas.append({"nome": tarefa_adicionada, "concluida": False})
    guardar_tarefas(tarefas)
    print("Tarefa Adicionada com sucesso!")


def concluir_tarefa(tarefas):

    if not tarefas:
        print("Não existem tarefas.")
        return

    mostrar_tarefas(tarefas)

    concluir = pedir_numero("Insira o numero da tarefa que pretende concluir: ")

    if 1 <= concluir <= len(tarefas):
        tarefas[concluir - 1]["concluida"] = True
        guardar_tarefas(tarefas)
        print("Tarefa concluida com sucesso!")
    else:
        print("Numero de tarefa inválido.")


def remover_tarefa(tarefas):

    if not tarefas:
        print("Não existem tarefas.")
        return

    mostrar_tarefas(tarefas)

    remover = pedir_numero("Insira o numero da tarefa que pretende remover: ")

    if 1 <= remover <= len(tarefas):
        tarefas.pop(remover - 1)
        guardar_tarefas(tarefas)
        print("Tarefa removida com sucesso!")
    else:
        print("Numero de tarefa invalido.")
