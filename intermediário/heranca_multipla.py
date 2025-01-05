class Animal:
    def __init__(self,nome):
        self.nome = nome
    
    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando."
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando."

class Morcego(Mamifero,Ave): # Herança multipla pois herda os atributos e metodos das duas classes
    def emitir_som(self):
        return "Morcegos emitem sons ultrassônicos"
    
morcego = Morcego(nome="Batman")

print(f"Nome: {morcego.nome}")

print(f"\nAcessando os medodos da classe Mamifero")
print(morcego.amamentar())
print(f"\nAcessando os medodos da classe Ave")
print(morcego.voar())
print(f"\nAcessando os medodos da classe Animal")
print(morcego.emitir_som())
