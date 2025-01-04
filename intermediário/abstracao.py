
#Abstração serve para preservar as caracteristica da classe, não é possivel criar uma instancia a partir dela, é apenas um molde para outras classes
from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def ligar (self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self):
        pass

    def ligar(self):
        return f'O Carro ligou usando a Chave'
    
    def desligar(self):
        return f'O Carro desligou usando a chave'
    
nissan_kicks = Carro()
print(nissan_kicks.ligar())
