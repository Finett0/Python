"""
    try: Para código que pode gerar erros.
    except: Para tratar os erros que surgirem.
    finally: Para executar ações que devem ocorrer sempre, com ou sem erros.
"""


while True:
    try:
        print("Exemplos de tratativa")
        num = int(input('Digite um numero: '))
        num2 = int(input('Digite mais um numero: '))
        resultado = num / num2   

    except ZeroDivisionError:
        print('Não é possivel fazer divisão por zero\n')

    except ValueError as erro_de_variavel:
        print(f'Erro de value error {erro_de_variavel}')
        raise  ValueError ("Tipo de variavel incompativeis")
    
    except Exception as error: 
        print(f'Erro:  {error}')

    else:
        print(f'A divisão entre {num} e {num2} = {resultado}')

    finally:
        print('Operação finalizada\n')

