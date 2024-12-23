#Loops são uma estrutura de controle que são executadas até que uma condição seja atendida

print('For com lista')
lista = [1,2,3,4,5]
for num in lista:
    print(num)

print('\nFor com tupla')

tupla = (1,2,3,4,5)

for num in tupla:
    print(num)

print('\nFor com dicionario - chaves')
pessoa = {'nome':'Giovanni','idade':20,'cidade':'São Paulo'}
for chave in pessoa.keys():
    print(chave)

print('\nFor com dicionario - valor')
for valor in pessoa.values():
    print(valor)

print('\nFor com todos os items do dicionarios')
for itens in pessoa.items():
    print(itens)

#Função range cria uma sequencia de numeros 

for num in range(6):
    print(f'Numero:{num}')

#Função len() retorna o numero de elementos em um obejto
lista = [1,2,3,4,5,6]
tamanho_lista = len(lista)
print(f'O tamanho da lista é {tamanho_lista} elementos')

#Função enumerate retorna o indice mais o valor do elemento
print('\n')
lista_e = ["A","B","C","D"]
for indice,valor in enumerate(lista_e):
    print(f'Indice: ',indice)
    print(f'Valor:',valor)
