from ficheiros import guardar_tarefas
from utils import pedir_numero, data_atual, formatar_data, pedir_prazo
from datetime import datetime

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

        prazo = tarefa["prazo"]
        estado_prazo_texto = estado_prazo(tarefa)

        if tarefa["prazo"] is None:
            prazo_formatado = "Sem prazo"
        else:
            prazo_formatado = formatar_data(tarefa["prazo"])

        estado = "[X]" if tarefa["concluida"] else "[ ]"
        data = formatar_data(tarefa["criada_em"])

        print(
            f"{i} - {estado} {tarefa['nome']} | "
            f"{tarefa['prioridade']} | {tarefa['categoria']}"
        )
        print(
            f"    {tarefa['descricao']} | "
            f"Criada: {data} | "
            f"Prazo: {prazo_formatado} | "
            f"Estado: {estado_prazo_texto}"
        )
        print()


def adicionar_tarefa(tarefas):
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    categoria = input("Categoria: ").strip().title()

    while True:
        confirmacao = input("Adicionar prazo? (s/n): ").strip().lower()

        if confirmacao == "s":
            prazo = pedir_prazo()
            break

        elif confirmacao == "n":
            prazo = None
            break

        else:
            print("Resposta inválida. Introduza 's' ou 'n'.")

    prioridade = pedir_prioridade()
    criada_em = data_atual()

    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "categoria": categoria,
        "prioridade": prioridade,
        "concluida": False,
        "criada_em": criada_em,
        "prazo": prazo,
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
        "5 - Prazo\n"
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

    elif editar_tipo == 5:
        print(
            "\nPrazo:\n"
            "1 - Definir/alterar prazo\n"
            "2 - Remover prazo\n"
            "0 - Cancelar"
        )

        opcao_prazo = pedir_numero("Opção: ")

        if opcao_prazo == 1:
            tarefa["prazo"] = pedir_prazo()

        elif opcao_prazo == 2:
            tarefa["prazo"] = None

        elif opcao_prazo == 0:
            return

        else:
            print("Opção inválida.")
            return

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
        "5 - Atrasadas\n"
        "6 - Sem Prazo\n"
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
    elif opcao == 5:
        filtrar_atrasadas(tarefas)
    elif opcao == 6:
        filtrar_sem_prazo(tarefas)
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


def estado_prazo(tarefa):
    prazo = tarefa["prazo"]

    if prazo is None:
        return "Sem prazo"

    prazo_data = datetime.strptime(prazo, "%Y-%m-%d %H:%M:%S")
    agora = datetime.now()

    if tarefa["concluida"]:
        return "Concluída"

    if esta_atrasada(tarefa):
        return "Atrasada"

    diferenca = prazo_data - agora
    segundos = int(diferenca.total_seconds())

    dias = segundos // 86400
    horas = segundos // 3600
    minutos = segundos // 60

    anos = dias // 365
    if anos >= 1:
        return "Falta 1 ano" if anos == 1 else f"Faltam {anos} anos"

    meses = dias // 30
    if meses >= 1:
        return "Falta 1 mês" if meses == 1 else f"Faltam {meses} meses"

    if dias >= 1:
        return "Falta 1 dia" if dias == 1 else f"Faltam {dias} dias"

    if horas >= 1:
        return "Falta 1 hora" if horas == 1 else f"Faltam {horas} horas"

    if minutos >= 1:
        return "Falta 1 minuto" if minutos == 1 else f"Faltam {minutos} minutos"

    return "Falta 1 segundo" if segundos == 1 else f"Faltam {segundos} segundos"


def filtrar_atrasadas(tarefas):
    resultados = []

    for tarefa in tarefas:
        if esta_atrasada(tarefa):
            resultados.append(tarefa)

    if not resultados:
        print("Não existem tarefas atrasadas.")
        return

    mostrar_tarefas(resultados)


def filtrar_sem_prazo(tarefas):
    resultados = []

    for tarefa in tarefas:
        if tarefa["prazo"] is None:
            resultados.append(tarefa)

    if not resultados:
        print("Não existem tarefas sem prazo.")
        return

    mostrar_tarefas(resultados)


def esta_atrasada(tarefa):
    prazo = tarefa["prazo"]

    if prazo is None:
        return False

    if tarefa["concluida"]:
        return False

    prazo_data = datetime.strptime(prazo, "%Y-%m-%d %H:%M:%S")

    return prazo_data < datetime.now()


def mostrar_estatisticas(tarefas):

    if not tarefas:
        print("Não existem tarefas.")
        return

    total = len(tarefas)
    concluidas = 0
    pendentes = 0
    atrasadas = 0
    sem_prazo = 0
    contagem_categorias = {}

    contagem_prioridades = {
        "Alta": 0,
        "Média": 0,
        "Baixa": 0,
    }

    for tarefa in tarefas:

        contagem_prioridades[tarefa["prioridade"]] += 1

        categoria = tarefa["categoria"]

        if categoria in contagem_categorias:
            contagem_categorias[categoria] += 1
        else:
            contagem_categorias[categoria] = 1

        if tarefa["concluida"]:
            concluidas += 1
        else:
            pendentes += 1

        if esta_atrasada(tarefa):
            atrasadas += 1

        if tarefa["prazo"] is None:
            sem_prazo += 1

    categoria_mais_usada = max(contagem_categorias, key=contagem_categorias.get)
    quantidade_categoria = contagem_categorias[categoria_mais_usada]
    taxa_conclusao = (concluidas / total) * 100
    com_prazo = total - sem_prazo

    print("===== Estatísticas =====\n")
    print("Total de tarefas:", total)
    print("\nPendentes:", pendentes)
    print("Concluídas:", concluidas)
    print("Atrasadas:", atrasadas)
    print("Com prazo:", com_prazo)
    print("Sem prazo:", sem_prazo)
    print("\nPrioridades:")
    print("Alta:", contagem_prioridades["Alta"])
    print("Média:", contagem_prioridades["Média"])
    print("Baixa:", contagem_prioridades["Baixa"])
    print(
        f"\nCategoria com mais tarefas: "
        f"{categoria_mais_usada} ({quantidade_categoria})"
    )
    print(f"\nTaxa de conclusão: {taxa_conclusao:.1f}%")
