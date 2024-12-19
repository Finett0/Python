#Só existe dois tipos de dados boleanos, o verdadeira e a falss

verdadeiro = True
falso = False

#Condicionais

# se a condição 2 > 1 for verdadeira ela ira cair no if, caso não seja vai cair no else
if 2 > 1:
    print(verdadeiro)
else:
    print(falso)

#Operadores Lógicos: and e or 

# No operador logico and as duas "verificações" precisam ser verdadeiras
if 2 > 1 and 1 < 2:
    print('\n Está condição é verdadeira')
else:
    print('Essa condição é falsa')

# No caso do or, apenas 1 condição precisa ser verdadeira
if "Giovanni" == "Gabriel" or 1000 > 100:
    print("Está condição tambem é verdadeira")
else:
    print("Está condição é falsa")

