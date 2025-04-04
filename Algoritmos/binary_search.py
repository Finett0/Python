"""
    A busca binária é um algoritomo utilizado para encontrar a posição de um elemento em uma lista ordenada
    Ele divide repetidamente o intervalo de busca pela metade até encontar o elemento procurado ou
    determinar que o elemento não está na lista
"""
def pesquisa_binaria(lista,item):
    baixo = 0
    alto = len(lista)-1 #Acompanham a parte da lista que você está procurando
    while baixo <= alto:#Enquanto ainda não conseguiu chegar a um único elemento
        meio = (baixo + alto) // 2 #verifiquei o elemento central
        chute = lista[meio]
        if chute == item: #Acha o item
            return meio
        if chute > item: #Chute foi muito alto
            alto = meio - 1
        else: #O chute foi muito baixo
            baixo = meio + 1
    return None

minha_lista = [1,3,5,7,9]

print(pesquisa_binaria(minha_lista,9))

