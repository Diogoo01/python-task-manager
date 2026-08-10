print("===== Gestor de Tarefas =====")
print("\n1 - Ver Tarefas ")
print("2 - Adicionar Tarefa")
print("3 - Concluir Tarefa")
print("4 - Remover Tarefa")
print("0 - Sair\n")

while True:
    escolha = int(input("Escolha: "))
    
    if escolha == 1:
        print("Mostrar Tarefas")
    elif escolha == 2:
        print("Adicionar Tarefa escolhido")
    elif escolha == 3:
        print("Tarefa concluida")
    elif escolha == 4:
        print("Tarefa removida com sucesso")
    elif escolha == 0:
        print("A sair...")
        break
    else:
        print("Por favor introduza um numero valido (0-4)")
