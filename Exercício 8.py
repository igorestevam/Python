# FUNÇÃO
def func (n):
    a = 0
    b = 1
    soma = a + b
    if(n == 1):
        return 0
    elif(n == 2):
        return 1
    for cont in range(2, n):
        c = a + b
        soma += c
        a = b
        b = c
    return soma
# PRINCIPAL
q = 0
while(q < 5):
    try:
        print('INFORME UM NÚMERO MAIOR QUE ZERO: ')
        n = int(input(f'{q + 1}º NÚMERO: '))
        if(n <= 0):
            print(f'ERRO: O NÚMERO INFORMADO DEVE SER MAIOR DO QUE ZERO.\n')
        else:
            print(f'A SOMA DOS {n} PRIMEIROS NÚMEROS DA SEQUÊNCIA DE FIBONACCI É: {func(n)}')
            q += 1
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')