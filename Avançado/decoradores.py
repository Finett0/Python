#Em resumo, Decoradores são funções que modificam a funcionalidade de outra função
def meu_decorador(func):
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada")

minha_funcao()
