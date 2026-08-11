import os
import json


# Guardar e carregar
def guardar_tarefas(tarefas):
    with open("tarefas.json", "w", encoding="utf-8") as ficheiro:
        # indent organiza o JSON e ensure_ascii=False mantém os caracteres legíveis
        json.dump(tarefas, ficheiro, indent=4, ensure_ascii=False)


def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as ficheiro:
            return json.load(ficheiro)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Menu
def mostrar_menu():
    print("===== Gestor de Tarefas =====")
    print("\n1 - Ver Tarefas ")
    print("2 - Adicionar Tarefa")
    print("3 - Concluir Tarefa")
    print("4 - Remover Tarefa")
    print("0 - Sair\n")


# Utilitários
def limpar_terminal():
    os.system("cls")


def pausar():
    input("\nPrima enter para continuar...")


def pedir_numero(mensagem):
    while True:
        try:
            escolha = int(input(mensagem))
            return escolha
        except ValueError:
            print("Por favor introduza um valor válido.")


# Lógica das tarefas
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


# Lista tarefas
tarefas = carregar_tarefas()

# Ciclo principal
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
