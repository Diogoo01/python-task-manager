import json


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
