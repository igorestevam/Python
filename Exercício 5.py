# FUNÇÃO
def lerPrimo (n):
    multiplos = 0
    if(n == 1 or n == 2 or n == 3):
        return 1
    else:
        for cont in range (2, n):
            if(n % cont == 0):
                multiplos += 1
        if(multiplos == 0):
            return 1
        else:
            return 0
# PRINCIPAL
q = 0
print('INFORME UM NÚMERO INTEIRO POSITIVO: ')
while(q < 500):
    try:
        n = int(input(f'{q + 1}º NÚMERO: '))
        if(n <= 0):
            print('ERRO: O NÚMERO INFORMADO DEVE SER MAIOR DO QUE ZERO.')
        else:
            if(lerPrimo(n) == 1):
                print(f'O NÚMERO {n} É PRIMO.')
            else:
                print(f'O NÚMERO {n} NÃO É PRIMO.')
            q += 1
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')