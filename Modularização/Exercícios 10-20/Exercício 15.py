# FUNÇÃO
def lerNum(a, q, n):
    An = a * q ** (n - 1)
    Sn = (a * ((q ** n) - 1)) / (q - 1)
    return An, Sn
# PRINCIPAL
quant = 0
while (quant < 50):
    try:
        print(f'{quant + 1}º PG: ')
        a = float(input('PRIMEIRO TERMO: '))
        q = float(input('RAZÃO: '))
        n = int(input('QUANTIDADE DE TERMOS: '))
        if(n <= 0):
            print(f'ERRO: A QUANTIDADE DE TERMOS DEVE SER MAIOR DO QUE ZERO.')
        else:
            print(f'ENÉSIMO TERMO (An): {lerNum(a, q, n)[0]: .2f}')
            print(f'SOMA DOS TERMOS (Sn): {lerNum(a, q, n)[1]:.2f}')
            quant += 1
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')