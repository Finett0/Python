
# Declarando a lista
lista_numerica = [1,2,3,4,5,6]
lista_texto = ['Giovanni','Erika', ' ']
lista_misturada = [1,2,3,'Giovanni','5',True,['Nova lista',2,10]]

lista_dentro_delista = [1,[2,[3,[4,[5,[6,[7,[8,[9,[10,[11,['Listas dentro de listas']]]]]]]]]]]]
print(lista_dentro_delista)


#exibindo elementos da Lista pelo indice
print("lista_misturada[0]: ",lista_misturada[0])
print("lista_mistuda[5]",lista_misturada[5])
print("lista_misturada[1:7]",lista_misturada[1:7]) #o nome disso é fatiamento, basicamente nos permite extrair uma porção especifica de uma lista
print("lista_misturada[:6]",lista_misturada[:6])
print("lista_misturada[:2]",lista_misturada[2:])


#Trocando elementos
lista_misturada[0] = 'Erika'
print(f'\nlista_misturada = {lista_misturada} ')

#Método append(): adiciona um elemento ao final da lista
lista_numerica.append(7)
print(f'\n')
print("lista_numerica.append(7)",lista_numerica)

#Metodo index retorna o indice do elemento 
indice = lista_numerica[0]
print(f'\nIndice 0 = {indice}')

#Metodo insert insero um elemento em um determinado indice
print(lista_numerica)
lista_numerica.insert(1,10)
print(f'\n lista_numerica.insert(1,10) {lista_numerica}')

#Metodo pop remove um elemento da lista, basta passar o indice -1
elemento_removido = lista_numerica.pop(1)
print(f"\n{elemento_removido}")
print(f'Lista numerica com o elemento removido {lista_numerica}')

#metodo remove 
lista_numerica.remove(7)
print(lista_numerica)

#metodo sort ele ordena de forma crescente a lista
lista_bagunçada = [2,1,4,6,7,8,112,1102,109,]

print(lista_bagunçada)
lista_bagunçada.sort()
print(f'Usando o metodo sort = {lista_bagunçada}')
