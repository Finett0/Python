class MeuDecoradorDeClasse:
    def __init__(self,func):
        self.func = func

    def __call__(self):
        print("Antes da minha função ser chamada (decorador de classe)")
        self.func()
        print("Depois da minha função ser chamada (decorador de classe)")

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda função")

segunda_funcao()
