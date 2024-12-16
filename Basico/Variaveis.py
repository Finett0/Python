# Não podemos declarar variaveis que a primeira letra tenha acentuação,caracteres especiais e numeros


nome_completo = 'Giovanni Finetto' #Note que você não precisa declarar o tipo da variavel, o python faz isso automaticamente e o nome disso é tipagem dinamica


nomeCompleto = 'Gabriel Finetto' #Python é uma linguagem Case sensitive, ela faz distinção de letras maisculas, estão a variavel nome_compleo é diferente de nome_Completo

print(nome_completo,nomeCompleto)

"""
    Note que a primeira variavel o espaço é substituido por um "_" esse tipo de conveção é chamada de Snake_Case
    Já no segundo caso, a conveção é a camelCase onde a primeira letra deve ser minúscula e a primeira letra de cada nova palavra maiúscula

    A recomendação é que a camelCase seja usada para classes e a Snake_Case seja usada para variaveis funções e metodos
"""
