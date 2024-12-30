# POO = Programação orientada a objetos

#Classe exemplo
class Pessoa:
    def __init__(self,nome,idade): #Init é o metodo construtor da classe
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f'Olá, meu nome é {self.nome} e eu tenho {self.idade} anos'
        
#Objetos é uma instancia da classe, ou seja, são criados a partir dessa classe
pessoa1 = Pessoa("Giovanni",20) #Criando uma instancia
mensagem = pessoa1.saudacao()
print(mensagem)

