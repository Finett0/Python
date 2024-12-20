#Dicionarios são estruturas de chave e valor {chave: valor}

#Declarando um dicionario
pessoa = {"nome":"Giovanni", "idade": 20, "meta":"ser progamador back-end"}

#acessando um dicionario
print("nome:",pessoa["nome"])
print("idade:",pessoa["idade"])
print(f"meta: {pessoa['meta']}")

#atribuindo uma chave e valor ao dicionario 
pessoa["cidade"] = "São paulo"
print("cidade",pessoa["cidade"])

#Deletar um par de chave e valor 
del pessoa["meta"]
print(pessoa)

#Metodos keys() values() items()

#keys() retona todas as chave do seu dicionario

chaves = pessoa.keys()
print(f"Chaves do meus dicionario: {chaves}")
#Caso queria acessar algum elemento em especifico eu preciso transformar em lista
chaves = list(pessoa.keys())
print(f"O Indice [0] do meu dicionario é:  {chaves[0]}")

#values() retorna os valores da sua lista
valores = pessoa.values()
print(f"Os valores da minha lista é {valores}")
#Caso queria ver o indice do valor, precisa transformar em lista


itens = pessoa.items()
print(f'Essse metodo basicamente retorna os dicinarios dentro de uma lista em que as chaves/valores estão dentro de tuplas {itens}')
