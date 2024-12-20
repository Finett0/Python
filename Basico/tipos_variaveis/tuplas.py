# Tuplas por definição são estruturas ordenadas e imutavel de elementos, vocÊ não pode remover ou adicionar 

minha_tupla = (1,2,3,4,2,2,2,4)

print(f'minha_tupla[0]: {minha_tupla[0]}')
print(f'minha_trupla[:2]: {minha_tupla[:2]}')
print(f'minha_tupla[-1]: {minha_tupla[-1]}')

#metodo count conta quantas vezes um determinado elemento apareceu em minha tupla

contagem = minha_tupla.count(2)
print(f"O 2 aparece {contagem} vezes em minha lista")

#Idex retorna o indice em que o elemento está dentro da tupla, funciona do mesmo jeito que nas listas

indice = minha_tupla.index(4)

print(f'O elemento 4 dentro da minha tupla está no indice {indice}')
