import json
from tarefa import Tarefa

FICHEIRO_TAREFAS = "tarefas.json"


def guardar_tarefas(tarefas):
    dados = []

    for tarefa in tarefas:
        dados.append(tarefa.para_dict())

    with open(FICHEIRO_TAREFAS, "w", encoding="utf-8") as ficheiro:
        json.dump(dados, ficheiro, indent=4, ensure_ascii=False)


def carregar_tarefas():
    try:
        with open(FICHEIRO_TAREFAS, "r", encoding="utf-8") as ficheiro:
            dados = json.load(ficheiro)

        tarefas = []

        for dados_tarefa in dados:
            tarefas.append(Tarefa.de_dict(dados_tarefa))

        return tarefas

    except (FileNotFoundError, json.JSONDecodeError):
        return []
