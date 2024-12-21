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
