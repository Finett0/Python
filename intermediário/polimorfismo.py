# Polimorfismo: Permite que os metodos se comportem de maneira diferente em classes distintas
class Animal:
    def __init__(self,nome):
        self.nome = nome

    def andar(self):
        return f"O {self.nome} andou"
    
    def som(self):
        pass
 
class Cachorro(Animal):
   def som(self): #Mesmo metodo, mas com comportamentos diferentes
       return f"é um cachorro e o som que ele faz é: 'Au au'"
    
class Gato(Animal):
    def som(self): #Mesma classe, mas com comportamentos diferentes
        return f"é um gato e som que ele faz é  'Miau, Miau'"
    
dog = Cachorro("Apollo")
cat = Gato ("Rogers")
animais = [dog,cat]
for animal in animais:
    print(f'O {animal.nome} {animal.som()}')
