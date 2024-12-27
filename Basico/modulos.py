
print('Importando modulos de terceiros')
print('\n Modulo math ')
import math #Importa o modulo inteiro 
     #ou
from math import sqrt # importa uma parte especifica

numero = int(input('Digite um numero: '))
raiz_quadrada = math.sqrt(numero)

print(f'A raiz quadrada do numero {numero} é {raiz_quadrada}')

print('Importando um modulo personalizado ')
from meus_modulos_personalizados import saudacao,dobro
mensagem = saudacao('Giovanni')
print(mensagem)
dobro_cinco = dobro(5)
print(f'O dobro do numero 5 é {dobro_cinco}')

