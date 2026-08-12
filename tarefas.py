from ficheiros import guardar_tarefas
from utils import pedir_numero, data_atual, formatar_data

PRIORIDADES = {
    1: "Alta",
    2: "Média",
    3: "Baixa",
}

ORDEM_PRIORIDADES = {valor: chave for chave, valor in PRIORIDADES.items()}


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

    while True:
        escolha = pedir_numero("Prioridade (1-Alta, 2-Média, 3-Baixa): ")

        if escolha in PRIORIDADES:
            return PRIORIDADES[escolha]

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
    categoria = input("Categoria: ").strip().title()

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
    if not tarefas:
        print("Não existem tarefas.")
        return

    mostrar_tarefas(tarefas)

    print("0 - Voltar")
    print("C - Remover todas as tarefas concluídas")

    escolha = input("Escolha: ").strip().lower()

    if escolha == "0":
        return

    elif escolha == "c":

        while True:
            confirmacao = input("Tem a certeza? (s/n): ").strip().lower()

            if confirmacao == "s":
                break

            elif confirmacao == "n":
                print("Operação cancelada.")
                return

            else:
                print("Resposta inválida. Introduza 's' ou 'n'.")

        pendentes = []

        for tarefa in tarefas:
            if not tarefa["concluida"]:
                pendentes.append(tarefa)

        if len(pendentes) == len(tarefas):
            print("Não existem tarefas concluídas.")
            return

        tarefas.clear()
        tarefas.extend(pendentes)

        guardar_tarefas(tarefas)
        print("Todas as tarefas concluídas foram removidas!")
        return

    try:
        numero = int(escolha)
    except ValueError:
        print("Opção inválida.")
        return

    if not 1 <= numero <= len(tarefas):
        print("Número de tarefa inválido.")
        return

    indice = numero - 1
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
        tarefa["categoria"] = input("Nova categoria: ").strip().title()

    elif editar_tipo == 4:
        tarefa["prioridade"] = pedir_prioridade()

    elif editar_tipo == 0:
        return

    else:
        print("Opção inválida.")
        return

    guardar_tarefas(tarefas)
    print("Tarefa alterada com sucesso!")


def pesquisar_tarefas(tarefas):
    texto = input("Pesquisar: ").lower()
    resultados = []

    for tarefa in tarefas:
        if (
            texto in tarefa["nome"].lower()
            or texto in tarefa["descricao"].lower()
            or texto in tarefa["categoria"].lower()
        ):
            resultados.append(tarefa)

    if not resultados:
        print("Nenhuma tarefa encontrada.")
        return

    mostrar_tarefas(resultados)


def filtrar_tarefas(tarefas):
    if not tarefas:
        print("Não existem tarefas.")
        return

    print(
        "\nFiltrar por:\n"
        "1 - Categoria\n"
        "2 - Prioridade\n"
        "3 - Pendentes\n"
        "4 - Concluídas\n"
        "0 - Voltar"
    )

    opcao = pedir_numero("Opção: ")

    if opcao == 1:
        filtrar_categoria(tarefas)
    elif opcao == 2:
        filtrar_prioridade(tarefas)
    elif opcao == 3:
        filtrar_estado(tarefas, False)
    elif opcao == 4:
        filtrar_estado(tarefas, True)
    elif opcao == 0:
        return
    else:
        print("Opção inválida.")


def filtrar_categoria(tarefas):
    categorias = []

    for tarefa in tarefas:
        categorias.append(tarefa["categoria"])

    categorias = sorted(set(categorias))

    print("Categorias disponíveis:")

    for i, categoria in enumerate(categorias, start=1):
        print(i, "-", categoria)

    opcao = pedir_numero("Categoria: ")

    if opcao == 0:
        return

    if not 1 <= opcao <= len(categorias):
        print("Opção inválida.")
        return

    categoria_escolhida = categorias[opcao - 1]

    resultados = []

    for tarefa in tarefas:
        if tarefa["categoria"] == categoria_escolhida:
            resultados.append(tarefa)

    mostrar_tarefas(resultados)


def filtrar_prioridade(tarefas):
    print("\nPrioridades:\n" "1 - Alta\n" "2 - Média\n" "3 - Baixa\n" "0 - Voltar")

    opcao = pedir_numero("Prioridade: ")

    if opcao == 0:
        return

    if opcao not in PRIORIDADES:
        print("Opção inválida.")
        return

    prioridade_escolhida = PRIORIDADES[opcao]

    resultados = []

    for tarefa in tarefas:
        if tarefa["prioridade"] == prioridade_escolhida:
            resultados.append(tarefa)

    mostrar_tarefas(resultados)


def filtrar_estado(tarefas, concluida):
    resultados = []

    for tarefa in tarefas:
        if tarefa["concluida"] == concluida:
            resultados.append(tarefa)

    if not resultados:
        estado = "concluídas" if concluida else "pendentes"
        print(f"Não existem tarefas {estado}.")
        return

    mostrar_tarefas(resultados)


def ordenar_tarefas(tarefas):
    if not tarefas:
        print("Não existem tarefas.")
        return

    print(
        "\nOrdenar por:\n"
        "1 - Data de criação (mais recentes)\n"
        "2 - Data de criação (mais antigas)\n"
        "3 - Nome (A-Z)\n"
        "4 - Nome (Z-A)\n"
        "5 - Prioridade (Alta-Baixa)\n"
        "6 - Prioridade (Baixa-Alta)\n"
        "7 - Categoria (A-Z)\n"
        "0 - Voltar"
    )

    opcao = pedir_numero("Opção: ")

    if opcao == 1:
        tarefas_ordenadas = sorted(
            tarefas, key=lambda tarefa: tarefa["criada_em"], reverse=True
        )
        mostrar_tarefas(tarefas_ordenadas)
    elif opcao == 2:
        tarefas_ordenadas = sorted(tarefas, key=lambda tarefa: tarefa["criada_em"])
        mostrar_tarefas(tarefas_ordenadas)

    elif opcao == 3:
        tarefas_ordenadas = sorted(tarefas, key=lambda tarefa: tarefa["nome"].lower())
        mostrar_tarefas(tarefas_ordenadas)

    elif opcao == 4:
        tarefas_ordenadas = sorted(
            tarefas, key=lambda tarefa: tarefa["nome"].lower(), reverse=True
        )
        mostrar_tarefas(tarefas_ordenadas)

    elif opcao == 5:
        tarefas_ordenadas = sorted(
            tarefas, key=lambda tarefa: ORDEM_PRIORIDADES[tarefa["prioridade"]]
        )
        mostrar_tarefas(tarefas_ordenadas)

    elif opcao == 6:
        tarefas_ordenadas = sorted(
            tarefas,
            key=lambda tarefa: ORDEM_PRIORIDADES[tarefa["prioridade"]],
            reverse=True,
        )
        mostrar_tarefas(tarefas_ordenadas)

    elif opcao == 7:
        tarefas_ordenadas = sorted(
            tarefas, key=lambda tarefa: tarefa["categoria"].lower()
        )
        mostrar_tarefas(tarefas_ordenadas)

    elif opcao == 0:
        return

    else:
        print("Opção inválida.")
