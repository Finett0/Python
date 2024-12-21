
"""
Condicionais servem para verificar algo e executar caso for verdadeiro
    if = se
    elife = se não se 
    else: se não 
"""
num = int(input('Digite um numero: '))

if num % 2 == 0:
    print(f'O numero {num} é par')
else:
    print(f'O numero {num} é impar')

#Condicional em uma linha
idade = int(input('Digite sua idade: '))
mensagem = 'Pode tirar carteira de motorista' if idade >= 18 else 'Infelizmente não pode tirar!'
print(mensagem)
