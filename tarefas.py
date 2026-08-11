from ficheiros import guardar_tarefas
from utils import pedir_numero, data_atual, formatar_data


def selecionar_tarefa(tarefas):
    if not tarefas:
        print("Não existem tarefas.")
        return None

    mostrar_tarefas(tarefas)

    numero = pedir_numero("Número da tarefa: ")

    if not 1 <= numero <= len(tarefas):
        print("Número de tarefa inválido.")
        return None

    return numero - 1


def pedir_prioridade():
    prioridades = {
        1: "Alta",
        2: "Média",
        3: "Baixa",
    }

    while True:
        escolha = pedir_numero("Prioridade (1-Alta, 2-Média, 3-Baixa): ")

        if escolha in prioridades:
            return prioridades[escolha]

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
    indice = selecionar_tarefa(tarefas)

    if indice is None:
        return

    tarefas[indice]["concluida"] = True
    guardar_tarefas(tarefas)
    print("Tarefa concluída com sucesso!")


def remover_tarefa(tarefas):
    indice = selecionar_tarefa(tarefas)

    if indice is None:
        return

    tarefas.pop(indice)
    guardar_tarefas(tarefas)
    print("Tarefa removida com sucesso!")


def limpar_tarefas(tarefas):
    if not tarefas:
        print("Não existem tarefas.")
        return

    while True:
        confirmacao = input("Tem a certeza? (s/n): ").lower()

        if confirmacao == "s":
            tarefas.clear()
            guardar_tarefas(tarefas)
            print("Todas as tarefas foram removidas!")
            return

        elif confirmacao == "n":
            print("Operação cancelada.")
            return

        else:
            print("Resposta inválida. Introduza 's' ou 'n'.")


def editar_tarefa(tarefas):
    indice = selecionar_tarefa(tarefas)

    if indice is None:
        return

    tarefa = tarefas[indice]

    print(
        "\nO que pretende editar?\n"
        "1 - Nome\n"
        "2 - Descrição\n"
        "3 - Categoria\n"
        "4 - Prioridade\n"
        "0 - Cancelar"
    )

    editar_tipo = pedir_numero("Opção: ")

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
