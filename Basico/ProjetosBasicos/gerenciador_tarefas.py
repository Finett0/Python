
def adicionar_tarefa(tarefas,nome_tarefa):
    tarefa = {"tarefas":nome_tarefa,"completada":False}
    tarefas.append(tarefa)
    print(f'Tarefa {nome_tarefa} foi adicionada com sucesso!')
    return
    

tarefa = []

while True:
    print("\nGerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar Tarefas completadas")
    print("6. Sair")

    escolha = int(input("Digite a sua escolha: "))
    
    if escolha == 1:
        nome_tarefa = input('Digite o nome da tarefa que deseja cadastrar: ')
        adicionar_tarefa(1,nome_tarefa)
    
    elif escolha == 6:
        print("Programa finalizado!")
        break
        
