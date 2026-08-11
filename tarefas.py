from ficheiros import guardar_tarefas
from utils import pedir_numero


def mostrar_tarefas(tarefas):
    if not tarefas:
        print("Não existem tarefas.")
        return

    for i, tarefa in enumerate(tarefas, start=1):

        estado = "[X]" if tarefa["concluida"] else "[ ]"

        print(
            f"{i} - {estado} {tarefa['nome']} | "
            f"{tarefa['prioridade']} | {tarefa['categoria']}"
        )
        print(f"    {tarefa['descricao']}")
        print()


def adicionar_tarefa(tarefas):
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    categoria = input("Categoria: ")

    while True:
        prioridade = pedir_numero("Prioridade (1-Alta, 2-Média, 3-Baixa): ")

        if prioridade == 1:
            prioridade = "Alta"
            break
        elif prioridade == 2:
            prioridade = "Média"
            break
        elif prioridade == 3:
            prioridade = "Baixa"
            break
        else:
            print("Prioridade inválida.")

    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "categoria": categoria,
        "prioridade": prioridade,
        "concluida": False,
    }

    tarefas.append(tarefa)
    guardar_tarefas(tarefas)
    print("Tarefa Adicionada com sucesso!")


def concluir_tarefa(tarefas):

    if not tarefas:
        print("Não existem tarefas.")
        return

    mostrar_tarefas(tarefas)

    concluir = pedir_numero("Número da tarefa: ")

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

    remover = pedir_numero("Número da tarefa: ")

    if 1 <= remover <= len(tarefas):
        tarefas.pop(remover - 1)
        guardar_tarefas(tarefas)
        print("Tarefa removida com sucesso!")
    else:
        print("Numero de tarefa invalido.")


def limpar_tarefas(tarefas):
    if not tarefas:
        print("Não existem tarefas.")
        return

    confirmacao = input("Tem a certeza? (s/n): ").lower()

    if confirmacao == "s":
        tarefas.clear()
        guardar_tarefas(tarefas)
        print("Todas as tarefas foram removidas!")
    else:
        print("Operação cancelada.")
