# FUNÇÃO
def lerTempo (ENTRADA, SAIDA):
    permH = SH - EH
    valor = permH * 7
    if(EH == SH):
        return permH, valor
    else:
        if(EM <= SM):
            return permH, valor
        else:
            permH -= 1
            valor = permH * 7
            return permH, valor
# PRINCIPAL
q = 0
print('INFORME O HORÁRIO DE ENTRADA E O DE SAÍDA DO ESTACIONAMENTO: ')
while (q < 3):
    try:
        print(f'{q + 1}º CARRO: ')
        ENTRADA = (input('HORÁRIO DE ENTRADA (HH:MM): '))
        EHM = ENTRADA.split(':')
        EH = int(EHM[0])
        EM = int(EHM[1])
        if(EH < 0 or EH >= 24):
            print(f'ERRO: AS HORAS DEVEM SER INFORMADAS ENTRE [0, 23].\n')
        elif(EM < 0 or EM >= 60):
            print(f'ERRO: OS MINUTOS INFORMADOS DEVEM ESTAR ENTRE [0, 59].\n')
        else:
            SAIDA = (input('HORÁRIO DE SAÍDA (HH:MM): '))
            SHM = SAIDA.split(':')
            SH = int(SHM[0])
            SM = int(SHM[1])
            if(SH < 0 or SH >= 24):
                print(f'ERRO: AS HORAS DEVEM SER INFORMADAS ENTRE [0, 23].\n')
            elif(SM < 0 or SM >= 60):
                print(f'ERRO: OS MINUTOS INFORMADOS DEVEM ESTAR ENTRE [0, 59].\n')
            elif(SH < EH or (SH == EH and SM < EM)):
                print(f'ERRO: O HORÁRIO DE SAÍDA NÃO PODE SER MENOR DO QUE O DE ENTRADA.\n')
            else:
                print(f'TEMPO DE PERMANÊNCIA: {lerTempo(ENTRADA, SAIDA) [0]} HORAS.')
                print(f'VALOR TOTAL A PAGAR: R${lerTempo(ENTRADA, SAIDA) [1]: .2f}\n')
                q += 1
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')