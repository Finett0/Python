nome = "Giovanni"
sobrenome = "Finetto"

nome_completo = "Giovanni Finetto"

#Metodo para transformar strings em minusculo


print(f"\nO metodo lower() deixa todas os carcteres da string em minusculo,como por exemplo nome.lower()",nome.lower()) #O metodo lower() deixa todas as letras em minusculo

print(f"\nO metodo upper() deixa todas os caracteres da string em caixa alta nome.upper()",nome.upper())

#Vale ressaltar que essas funções não alteram o valor que está armazenando a variavel

#para acessar algum caracter especifico em uma variavel basta colocar [] na frente da variavel e dentro indice numerico do valor, lembrando que em python o indice sempre começa em zero

print(nome[0]) # Printar apenas o G
 
print(nome[0:5]) # ira exibir todos os caracter o indice 0 até o 5


# Metodo count(" ") é usado para contar quantas vezes um elemento aparece em uma variavel 

print(f"Dentro da variavel o caracter 'n' aparece: {nome_completo.count("n")} vezes")

#metodo find(" ") retorna o indice do elemento passado como parametro

print(nome_completo.find("n"))


# replace("","") substitui um caracter pelo outro 

print(nome_completo.replace("G","T").replace("F","R"))

#join() acresenta o caracter definido na frente de outro caracter da variavel

print("-".join(nome_completo))

#metodo split basicamente separa uma string a partir de um caracter definido

print(nome_completo.split(" "))


#metodo strip remove apenas os caracters que estão no começo e no final
nome_errado = 'xGiovanni Finettox'

print(f"\n",nome_completo.strip("x"))

 