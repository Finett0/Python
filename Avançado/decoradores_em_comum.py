class MinhaClasse:
    valor = 10 # Atributo de classe, você não precisa de uma instancia para acessar esse atributo 

    def __init__(self,nome): #Metodo construtor, o "self recebe a instancia"
        self.nome = nome # Atributo da instância, você precisa declarar uma instancia para chamar esse atributo 

    
    def metodo_instancia(self): #Requer uma instancia para ser chamado
        return f"Método de instancia chamado para {self.nome}"
    
    @classmethod  
    def metodo_classe(cls): #Recebe a classe como primeiro argumento e não precisa de uma instancia para ser chamado
        return f"Método de classe chamado para valor={cls.valor}"
    
    @staticmethod
    def metodo_estatico():#Não recebe nenhum argumento, portanto, nao tem acesso aos atributos da instancia e da classe
        return "Método estático chamado"
        

print(f'Acessando o atributo da minha classe: MinhaClasse.valor() = {MinhaClasse.valor}')
obj = MinhaClasse('obj')
print(f"Para acessar o atributo da minha instancia eu preciso declaralo: obj = MinhaClasse('obj')")
print(f"Acessando o atributo nome da minha instancia: obj.nome = {obj.nome} ")

print(MinhaClasse.metodo_estatico())


class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca #Atributos de classe?
        self.modelo = modelo #Atributos de classe?
        self.ano = ano #Atributos de classe?
    
    @classmethod
    def criar_carro(cls,configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca,modelo,int(ano))

configuracao1 = "Toyota,corrola,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"\nMarca: {carro1.marca}\nModelo:{carro1.modelo}\nAno: {carro1.ano}")
