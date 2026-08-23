from ficheiros import carregar_tarefas, guardar_tarefas
from utils import formatar_data, pedir_numero, pedir_prazo
from tarefa import Tarefa

PRIORIDADES = {
    1: "Alta",
    2: "Média",
    3: "Baixa",
}

ORDEM_PRIORIDADES = {valor: chave for chave, valor in PRIORIDADES.items()}


class GestorTarefas:
    def __init__(self):
        self.tarefas = carregar_tarefas()

    def mostrar_tarefas(self, tarefas=None):
        if tarefas is None:
            tarefas = self.tarefas

        if not tarefas:
            print("Não existem tarefas.")
            return

        for i, tarefa in enumerate(tarefas, start=1):
            estado_prazo_texto = tarefa.estado_prazo()

            if tarefa.prazo is None:
                prazo_formatado = "Sem prazo"
            else:
                prazo_formatado = formatar_data(tarefa.prazo)

            estado = "[X]" if tarefa.concluida else "[ ]"
            data = formatar_data(tarefa.criada_em)

            print(
                f"{i} - {estado} {tarefa.nome} | "
                f"{tarefa.prioridade} | {tarefa.categoria}"
            )

            print(
                f"    {tarefa.descricao} | "
                f"Criada: {data} | "
                f"Prazo: {prazo_formatado} | "
                f"Estado: {estado_prazo_texto}"
            )

            print()

    def selecionar_tarefa(self):
        if not self.tarefas:
            print("Não existem tarefas.")
            return None

        self.mostrar_tarefas()

        numero = pedir_numero("Número da tarefa: ")

        if not 1 <= numero <= len(self.tarefas):
            print("Número de tarefa inválido.")
            return None

        return numero - 1

    def concluir_tarefa(self):
        indice = self.selecionar_tarefa()

        if indice is None:
            return

        self.tarefas[indice].concluir()

        guardar_tarefas(self.tarefas)
        print("Tarefa concluída com sucesso!")

    def pedir_prioridade(self):
        while True:
            escolha = pedir_numero("Prioridade (1-Alta, 2-Média, 3-Baixa): ")

            if escolha in PRIORIDADES:
                return PRIORIDADES[escolha]

            print("Prioridade inválida.")

    def adicionar_tarefa(self):
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

        prioridade = self.pedir_prioridade()

        tarefa = Tarefa(
            nome,
            descricao,
            categoria,
            prioridade,
            prazo,
        )

        self.tarefas.append(tarefa)

        guardar_tarefas(self.tarefas)
        print("Tarefa adicionada com sucesso!")

    def remover_tarefa(self):
        if not self.tarefas:
            print("Não existem tarefas.")
            return

        self.mostrar_tarefas()

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

            for tarefa in self.tarefas:
                if not tarefa.concluida:
                    pendentes.append(tarefa)

            if len(pendentes) == len(self.tarefas):
                print("Não existem tarefas concluídas.")
                return

            self.tarefas.clear()
            self.tarefas.extend(pendentes)

            guardar_tarefas(self.tarefas)
            print("Todas as tarefas concluídas foram removidas!")
            return

        try:
            numero = int(escolha)
        except ValueError:
            print("Opção inválida.")
            return

        if not 1 <= numero <= len(self.tarefas):
            print("Número de tarefa inválido.")
            return

        indice = numero - 1
        self.tarefas.pop(indice)

        guardar_tarefas(self.tarefas)
        print("Tarefa removida com sucesso!")

    def limpar_tarefas(self):
        if not self.tarefas:
            print("Não existem tarefas.")
            return

        while True:
            confirmacao = input("Tem a certeza? (s/n): ").strip().lower()

            if confirmacao == "s":
                self.tarefas.clear()
                guardar_tarefas(self.tarefas)
                print("Todas as tarefas foram removidas!")
                return

            elif confirmacao == "n":
                print("Operação cancelada.")
                return

            else:
                print("Resposta inválida. Introduza 's' ou 'n'.")

    def editar_tarefa(self):
        indice = self.selecionar_tarefa()

        if indice is None:
            return

        tarefa = self.tarefas[indice]

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
            tarefa.nome = input("Novo nome: ")

        elif editar_tipo == 2:
            tarefa.descricao = input("Nova descrição: ")

        elif editar_tipo == 3:
            tarefa.categoria = input("Nova categoria: ").strip().title()

        elif editar_tipo == 4:
            tarefa.prioridade = self.pedir_prioridade()

        elif editar_tipo == 5:
            print(
                "\nPrazo:\n"
                "1 - Definir/alterar prazo\n"
                "2 - Remover prazo\n"
                "0 - Cancelar"
            )

            opcao_prazo = pedir_numero("Opção: ")

            if opcao_prazo == 1:
                tarefa.prazo = pedir_prazo()

            elif opcao_prazo == 2:
                tarefa.prazo = None

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

        guardar_tarefas(self.tarefas)
        print("Tarefa alterada com sucesso!")

    def pesquisar_tarefas(self):
        texto = input("Pesquisar: ").lower()
        resultados = []

        for tarefa in self.tarefas:
            if (
                texto in tarefa.nome.lower()
                or texto in tarefa.descricao.lower()
                or texto in tarefa.categoria.lower()
            ):
                resultados.append(tarefa)

        if not resultados:
            print("Nenhuma tarefa encontrada.")
            return

        self.mostrar_tarefas(resultados)

    def filtrar_tarefas(self):
        if not self.tarefas:
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
            self.filtrar_categoria()
        elif opcao == 2:
            self.filtrar_prioridade()
        elif opcao == 3:
            self.filtrar_estado(False)
        elif opcao == 4:
            self.filtrar_estado(True)
        elif opcao == 5:
            self.filtrar_atrasadas()
        elif opcao == 6:
            self.filtrar_sem_prazo()
        elif opcao == 0:
            return
        else:
            print("Opção inválida.")

    def filtrar_categoria(self):
        categorias = []

        for tarefa in self.tarefas:
            categorias.append(tarefa.categoria)

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

        for tarefa in self.tarefas:
            if tarefa.categoria == categoria_escolhida:
                resultados.append(tarefa)

        self.mostrar_tarefas(resultados)

    def filtrar_prioridade(self):
        print("\nPrioridades:\n" "1 - Alta\n" "2 - Média\n" "3 - Baixa\n" "0 - Voltar")

        opcao = pedir_numero("Prioridade: ")

        if opcao == 0:
            return

        if opcao not in PRIORIDADES:
            print("Opção inválida.")
            return

        prioridade_escolhida = PRIORIDADES[opcao]

        resultados = []

        for tarefa in self.tarefas:
            if tarefa.prioridade == prioridade_escolhida:
                resultados.append(tarefa)

        self.mostrar_tarefas(resultados)

    def filtrar_estado(self, concluida):
        resultados = []

        for tarefa in self.tarefas:
            if tarefa.concluida == concluida:
                resultados.append(tarefa)

        if not resultados:
            estado = "concluídas" if concluida else "pendentes"
            print(f"Não existem tarefas {estado}.")
            return

        self.mostrar_tarefas(resultados)

    def filtrar_atrasadas(self):
        resultados = []

        for tarefa in self.tarefas:
            if tarefa.esta_atrasada():
                resultados.append(tarefa)

        if not resultados:
            print("Não existem tarefas atrasadas.")
            return

        self.mostrar_tarefas(resultados)

    def filtrar_sem_prazo(self):
        resultados = []

        for tarefa in self.tarefas:
            if tarefa.prazo is None:
                resultados.append(tarefa)

        if not resultados:
            print("Não existem tarefas sem prazo.")
            return

        self.mostrar_tarefas(resultados)

    def ordenar_tarefas(self):
        if not self.tarefas:
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
                self.tarefas,
                key=lambda tarefa: tarefa.criada_em,
                reverse=True,
            )

        elif opcao == 2:
            tarefas_ordenadas = sorted(
                self.tarefas,
                key=lambda tarefa: tarefa.criada_em,
            )

        elif opcao == 3:
            tarefas_ordenadas = sorted(
                self.tarefas,
                key=lambda tarefa: tarefa.nome.lower(),
            )

        elif opcao == 4:
            tarefas_ordenadas = sorted(
                self.tarefas,
                key=lambda tarefa: tarefa.nome.lower(),
                reverse=True,
            )

        elif opcao == 5:
            tarefas_ordenadas = sorted(
                self.tarefas,
                key=lambda tarefa: ORDEM_PRIORIDADES[tarefa.prioridade],
            )

        elif opcao == 6:
            tarefas_ordenadas = sorted(
                self.tarefas,
                key=lambda tarefa: ORDEM_PRIORIDADES[tarefa.prioridade],
                reverse=True,
            )

        elif opcao == 7:
            tarefas_ordenadas = sorted(
                self.tarefas,
                key=lambda tarefa: tarefa.categoria.lower(),
            )

        elif opcao == 0:
            return

        else:
            print("Opção inválida.")
            return

        self.mostrar_tarefas(tarefas_ordenadas)

    def mostrar_estatisticas(self):
        if not self.tarefas:
            print("Não existem tarefas.")
            return

        total = len(self.tarefas)
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

        for tarefa in self.tarefas:
            contagem_prioridades[tarefa.prioridade] += 1

            categoria = tarefa.categoria

            if categoria in contagem_categorias:
                contagem_categorias[categoria] += 1
            else:
                contagem_categorias[categoria] = 1

            if tarefa.concluida:
                concluidas += 1
            else:
                pendentes += 1

            if tarefa.esta_atrasada():
                atrasadas += 1

            if tarefa.prazo is None:
                sem_prazo += 1

        categoria_mais_usada = max(
            contagem_categorias,
            key=contagem_categorias.get,
        )

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
