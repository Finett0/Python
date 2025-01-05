#Um decorador é um tipo especial de função que recebe outra função como entrada e, em seguida, retorna uma nova função que geralmente envolve a função original.
def meu_decorador(func):
    def wrapper(): #wrapper é um pedaço de código que é usado para modificar ou estender o comportamento de uma função, método ou classe existente sem modificar seu código-fonte. 
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada")

minha_funcao()
