def exibir_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa na lista.")
    else:
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa a ser adicionada: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def remover_tarefa(tarefas):
    exibir_tarefas(tarefas)
    indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
    if 0 <= indice < len(tarefas):
        tarefa_removida = tarefas.pop(indice)
        print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
    else:
        print("Índice inválido.")

def menu():
    tarefas = []
    while True:
        print("\nMenu de Lista de Tarefas")
        print("1. Exibir Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Remover Tarefa")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            exibir_tarefas(tarefas)
        elif opcao == '2':
            adicionar_tarefa(tarefas)
        elif opcao == '3':
            remover_tarefa(tarefas)
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()
