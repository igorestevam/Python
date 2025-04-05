# FUNÇÃO
def lerIMC(altura, massa, sexo):
    if(sexo == 1):
        return (0.95 * massa) / (altura ** 2)
    else:
        return (1.05 * massa) / (altura ** 2)
# PRINCIPAL
q = 0   
while(q < 3):
    try:
        print(f'{q + 1}º ENTREVISTADO:')
        altura = float(input('ALTURA (M): '))
        if(altura <= 0):
            print(f'ERRO: A ALTURA INFORMADA DEVE SER MAIOR DO QUE 0.\n')
        else:
            massa = float(input('MASSA (KG): '))
            if(massa <= 0):
                print(f'ERRO: A MASSA INFORMADA DEVE SER MAIOR DO QUE 0.\n')
            else:
                sexo = int(input('SEXO [1 = FEM, 2 = MASC]: '))
                if(sexo != 1 and sexo != 2):
                    print(f'ERRO: O SEXO DEVE SER INFORMADO POR [1 ou 2].\n')
                else:
                    print(f'IMC: {lerIMC(altura, massa, sexo): .2f}\n')
                    q += 1
    except Exception as ERRO_EXCECAO:
        print(f'ERRO D EXCEÇÃO: {ERRO_EXCECAO}')