class Animal:
    def __init__(self,nome):
        self.nome = nome

    def andar(self):
        return f"O {self.nome} andou"
    
 
class Cachorro(Animal): #Herdou os atributos e metodos da classe cachorro
    pass
    
apollo = Cachorro(nome="Apollo")
print(apollo.andar())
