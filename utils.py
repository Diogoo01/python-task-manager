import os
from datetime import datetime


def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPrima enter para continuar...")


def pedir_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Por favor introduza um valor válido.")


def data_atual():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def formatar_data(data_texto):
    data = datetime.strptime(data_texto, "%Y-%m-%d %H:%M:%S")
    return data.strftime("%d/%m/%Y %H:%M")


def pedir_prazo():
    while True:
        texto = input("Prazo (dd/mm/aaaa hh:mm): ")

        try:
            prazo = datetime.strptime(texto, "%d/%m/%Y %H:%M")
            return prazo.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Data ou hora inválida.")
