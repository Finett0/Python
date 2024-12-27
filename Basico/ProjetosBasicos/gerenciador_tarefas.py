def adicionar_tarefa(tarefas,nome_tarefa):
    tarefa = {"tarefa":nome_tarefa, "completada":False}
    tarefas.append(tarefa)
    print(f"\nTarefa {nome_tarefa} foi adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    print("\nLista de Tarefas")
    for indice,tarefa in enumerate(tarefas,start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f'{indice}. - [{status}] {nome_tarefa}')

def atualizar_nome_tarefa(tarefas,indice_tarefa,novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):   
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f'Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}')
    else:
        print("indice de tarefa invalido!")

def completar_tarefa(tarefas,indice_tarefa):
    indice_tarefa_ajustado = indice_tarefa - 1 
    tarefas[indice_tarefa_ajustado]["completada"] = True
    print(f'Tarefa {indice_tarefa} marcada como completada')
    return

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print('Tarefas Completadas foram deletadas com sucesso!')
tarefas = []
while True:
    print("\nMenu Gerenciador de Tarefas\n")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar Tarefas completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")
    
    if escolha == "1":
        nome_tarefa = input("\nDigite o nome da tarefa que quer adicionar: ")
        adicionar_tarefa(tarefas,nome_tarefa)

    elif escolha == "2":
        ver_tarefas(tarefas)
    
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o numero da tarefa que deseja atualizar: ")
        novo_nome = input ("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas,indice_tarefa,novo_nome)

    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = int(input("Digite o numero da tarefa que deseja completar: "))
        completar_tarefa(tarefas,indice_tarefa)

    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)

    elif escolha == "6":
        print("Programa finalizado!")
        break
        

