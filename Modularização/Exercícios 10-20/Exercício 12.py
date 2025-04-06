import math
# FUNÇÃO
def lerSeg (seg):
    hora = math.floor(seg / 3600)
    minuto = math.floor(((seg / 3600) - hora) * 60)
    segundo = math.ceil((((seg / 3600) - hora) * 60 - minuto) * 60)
    return hora, minuto, segundo
# PRINCIPAL
q = 0
print('INFORME, EM SEGUNDOS, O TEMPO LEVADO PARA REALIZAR O TESTE DO LABORATÓRIO:')
while(q < 100):
    try:
        print(f'{q + 1}º TESTE: ')
        seg = int(input('TEMPO (SEG): '))
        if(seg <= 0):
            print(f'ERRO: O TEMPO INFORMADO DEVE SER MAIOR DO QUE ZERO.\n')
        else:
            print(f'TEMPO LEVADO PARA FAZER O TESTE: {lerSeg(seg) [0]} HORA(S) + {lerSeg(seg) [1]} MINUTO(S) + {lerSeg(seg) [2]} SEGUNDO(S).')
            q += 1
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')