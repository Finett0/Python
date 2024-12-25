#Aplicação em desenvolvimento
import os

def exibir_programa():
    print('\nQUIZ PYTHON!\n-------------')

def apresentar():
    print('Olá Pessoa Desenvolvedora,bora testar seus conhecimentos em python?')
    nome = input('\nPrimeiramente digite seu nome: ')
    print(f'\n{nome}, qual o seu nivel de conhecimento em python? ')

def Nivel_Python():
    print('\n 1º para Basico\n 2º para Intermediario\n 3º para Avançado')
    num_nivel = int(input('\nDigite aqui: '))
    if num_nivel == 1:
        os.system('clear')
        print('\nVamos Testar seu nivel Basico de Python!\n')
        basico()
    elif num_nivel == 2:
        os.system('clear')
        print('Vamos Testar o seu nivel Intermediario de Python!\n')
    else:
        os.system('clear')
        print('Vamos testar seu nivel Avançado de Python\n')

def basico():
    print('O que são variaveis?')
    variaveis_opcao1 = '1º - Um conjunto numerico'
    variaveis_opcao2 = '2º - Espaço na memoria do seu computador em que algo é armazendo'
    variaveis_opcao3 = '3º - Textos'
    print(f'\n OPÇÕES:\n {variaveis_opcao1}\n {variaveis_opcao2}\n {variaveis_opcao3}')
    resposta_variaveis = int(input('\nDigite opção correta: '))

    def tentar_novamentep1():
        resposta_variaveis = int(input('\nDigite opção correta: '))
        if resposta_variaveis == 2:
             segunda_pergunta()
        else:
            print('Resposta errada, tente novamente !')
            tentar_novamentep1()


    if resposta_variaveis == 2:
        segunda_pergunta()
    else:
        print('Resposta errada, tente novamente !')
        tentar_novamentep1()

def segunda_pergunta():
    print('Parabens você acertou\nVamos para a proxima pergunta!')
    


def main():
    os.system('clear')


if __name__ == '__main__':
    main()
    exibir_programa()
    apresentar()
    Nivel_Python()
