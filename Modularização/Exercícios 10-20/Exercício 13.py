import math
# FUNÇÃO
def lerHora(T):
    hora = math.floor(T)
    minuto = math.floor((T - math.floor(T)) * 60)
    segundo = math.floor((((T - math.floor(T)) * 60) - minuto)* 60)
    return hora, minuto, segundo
# PRINCIPAL
q = 0
print('INFORME O TEMPO EM HORAS: ')
while(q < 50):
    try:
        print(f'{q + 1}º TEMPO: ')
        T = float(input('HORAS: '))
        if(T <= 0):
            print(f'ERRO: O TEMPO INFORMADO DEVE SER MAIOR DO QUE 0.\n')
        else:
            print(f'HORÁRIO: {lerHora(T) [0]} HORA(S) + {lerHora(T) [1]} MINUTO(S) + {lerHora(T) [2]} SEGUNDO(S).\n')
            q += 1
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')