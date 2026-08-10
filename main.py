def mostrar_tarefas(tarefas):
    if not tarefas:
        print("Não existem tarefas.")
        return

    for i, tarefa in enumerate(tarefas, start=1):
        estado = "[X]" if tarefa["concluida"] else "[ ]"
        print(i, "-", estado, tarefa["nome"])



print("===== Gestor de Tarefas =====")
print("\n1 - Ver Tarefas ")
print("2 - Adicionar Tarefa")
print("3 - Concluir Tarefa")
print("4 - Remover Tarefa")
print("0 - Sair\n")

tarefas = []

while True:

    escolha = int(input("Escolha: "))
    
    if escolha == 1:
        mostrar_tarefas(tarefas)

    elif escolha == 2:
        tarefa_adicionada = input("Insira o nome da tarefa que pretende adicionar: ")
        tarefas.append({"nome": tarefa_adicionada, "concluida": False}) 
        print("Tarefa Adicionada com sucesso!")

    elif escolha == 3:

        if not tarefas:
            print("Não existem tarefas.")
            continue

        mostrar_tarefas(tarefas)

        concluir = int(input("Insira o numero da tarefa que pretende concluir: "))

        if 1 <= concluir <= len(tarefas):
            tarefas[concluir - 1]["concluida"] = True
            print("Tarefa concluida com sucesso!")
        else:
            print("Numero de tarefa inválido.")

    elif escolha == 4:

        if not tarefas:
            print("Não existem tarefas.")
            continue

        mostrar_tarefas(tarefas)

        remover = int(input("Insira o numero da tarefa que pretende remover: "))

        if 1 <= remover <= len(tarefas):
            tarefas.pop(remover-1)
            print("Tarefa removida com sucesso!")
        else:
            print("Numero de tarefa invalido.")

    elif escolha == 0:
        print("A sair...")
        break

    else:
        print("Por favor introduza um numero valido (0-4)")
