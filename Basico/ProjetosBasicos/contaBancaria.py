class ContaBancaria:
    def __init__(self,numeroConta,titular,saldo):
        self.__titular = titular
        self.__saldo = saldo
        self.__numeroConta = numeroConta
        

    def get_titular(self):
        return self.__titular
    
    def get_saldo(self):
        return self.__saldo
    
    def get_conta(self):
        return self.__numeroConta
    
    def depositar(self,numeroConta,valor):
        if valor > 0 and numeroConta == self.__numeroConta:
            self.__saldo += valor
            return self.__saldo

    def sacar(self,numeroConta,valor):
        if valor <= self.__saldo and numeroConta == self.__numeroConta:
            self.__saldo -= valor
            return self.__saldo
        
    def consultarSaldo(self,numeroConta):
        if numeroConta == self.__numeroConta:
            return self.__saldo
        

giovanni = ContaBancaria(numeroConta=55264,titular="Giovanni",saldo=1000,)

print(giovanni.get_titular(),giovanni.get_conta(),giovanni.get_saldo())

giovanni.depositar(55264,1000)
print(giovanni.consultarSaldo(55264))
giovanni.sacar(55264,1500)
print(giovanni.consultarSaldo(55264))

