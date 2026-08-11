import os


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
