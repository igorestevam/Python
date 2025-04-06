# FUNÇÃO
def lerTri(A, B, C):
    if(A < B + C and B < A + C and C < A + B):
        if(A == B and B == C):
            return 1
        elif((A == B and B != C) or (A == C and C != B) or (B == C and C != A)):
            return 2
        else:
            return 3
    else:
        return 0
# PRINCIPAL
q = 0
while True:
    try:
        print('MENU DO PROGRAMA:')
        print('OPÇÃO 1: INICIAR')
        print('QUALQUER TECLA: FINALIZAR')
        menu = int(input())
        if(menu != 1):
            print(f'FIM DO PROGRAMA!')
            break
        else:
            print(f'\nINFORME OS LADOS DO {q + 1}º TRIÂNGULO: ')
            A = float(input('LADO A: '))
            B = float(input('LADO B: '))
            C = float(input('LADO C: '))
            if(lerTri(A, B, C) == 0):
                print(f'NÃO É UM TRIÂNGULO!\n')
            elif(lerTri(A, B, C) == 1):
                print(f'É UM TRIÂNGULO EQUILÁTERO.\n')
            elif(lerTri(A, B, C) == 2):
                print(f'É UM TRIÂNGULO ISÓSCELE.\n')
            else:
                print(f'É UM TRIÂNGULO ESCALENO.\n')
            q += 1
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')