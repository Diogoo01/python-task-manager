print("===== Gestor de Tarefas =====")
print("\n1 - Ver Tarefas ")
print("2 - Adicionar Tarefa")
print("3 - Concluir Tarefa")
print("4 - Remover Tarefa")
print("0 - Sair\n")

tarefas = []
i = 1

while True:

    escolha = int(input("Escolha: "))
    
    if escolha == 1:
        if not tarefas:
            print("Não existem tarefas.")
        else:
            for tarefa in tarefas:
                print(i, "-", tarefa)
                i += 1
    elif escolha == 2:
        tarefa_adicionada = input("Insira o nome da tarefa que pretende adicionar: ")
        tarefas.append(tarefa_adicionada)
        print("Tarefa Adicionada com sucesso!")

    elif escolha == 3:
        print("Tarefa concluida")
    elif escolha == 4:
        print("Tarefa removida com sucesso")
    elif escolha == 0:
        print("A sair...")
        break
    else:
        print("Por favor introduza um numero valido (0-4)")
