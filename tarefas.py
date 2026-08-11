from ficheiros import guardar_tarefas
from utils import pedir_numero, data_atual, formatar_data


def pedir_prioridade():
    while True:
        prioridade = pedir_numero("Prioridade (1-Alta, 2-Média, 3-Baixa): ")

        if prioridade == 1:
            return "Alta"
        elif prioridade == 2:
            return "Média"
        elif prioridade == 3:
            return "Baixa"
        else:
            print("Prioridade inválida.")


def mostrar_tarefas(tarefas):
    if not tarefas:
        print("Não existem tarefas.")
        return

    for i, tarefa in enumerate(tarefas, start=1):

        estado = "[X]" if tarefa["concluida"] else "[ ]"
        data = formatar_data(tarefa["criada_em"])

        print(
            f"{i} - {estado} {tarefa['nome']} | "
            f"{tarefa['prioridade']} | {tarefa['categoria']}"
        )
        print(f"    {tarefa['descricao']} | Criada: {data}")
        print()


def adicionar_tarefa(tarefas):
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    categoria = input("Categoria: ")

    prioridade = pedir_prioridade()
    criada_em = data_atual()

    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "categoria": categoria,
        "prioridade": prioridade,
        "concluida": False,
        "criada_em": criada_em,
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


def editar_tarefa(tarefas):
    if not tarefas:
        print("Não existem tarefas.")
        return

    mostrar_tarefas(tarefas)

    editar_numero = pedir_numero("Número da tarefa: ")

    if not 1 <= editar_numero <= len(tarefas):
        print("Número de tarefa inválido.")
        return

    print(
        "\nO que pretende editar?\n"
        "1 - Nome\n"
        "2 - Descrição\n"
        "3 - Categoria\n"
        "4 - Prioridade\n"
        "0 - Cancelar"
    )

    editar_tipo = pedir_numero("Opção: ")

    tarefa = tarefas[editar_numero - 1]

    if editar_tipo == 1:
        tarefa["nome"] = input("Novo nome: ")

    elif editar_tipo == 2:
        tarefa["descricao"] = input("Nova descrição: ")

    elif editar_tipo == 3:
        tarefa["categoria"] = input("Nova categoria: ")

    elif editar_tipo == 4:
        tarefa["prioridade"] = pedir_prioridade()

    elif editar_tipo == 0:
        return

    else:
        print("Opção inválida.")
        return

    guardar_tarefas(tarefas)
    print("Tarefa alterada com sucesso!")
