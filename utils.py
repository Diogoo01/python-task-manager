import os
from datetime import datetime


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


def data_atual():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def formatar_data(data_texto):
    data = datetime.strptime(data_texto, "%Y-%m-%d %H:%M:%S")
    return data.strftime("%d/%m/%Y %H:%M")
