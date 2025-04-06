# FUNÇÃO
def lerSalario (salario, dependente):
    descontos = (salario * 11 / 100) + (salario * 2 / 100)
    salLiquido = salario - descontos + (1518 + ((salario * 5 / 100) * dependente))
    return salLiquido, descontos
# PRINCIPAL
q = 0
while True:
    try:
        print('MENU DO PROGRAMA: ')
        print('OPÇÃO 1: INICIAR.')
        print('QUALQUER OUTRA TECLA: FINALIZAR.')
        menu = int(input(''))
        if(menu != 1):
            print('FIM DO PROGRAMA!')
            break
        else:
            print(f'\n{q + 1}º CONTRACHEQUE: ')
            salario = float(input('SALÁRIO BRUTO: '))
            if(salario <= 0):
                print(f'ERRO: O SALÁRIO INFORMADO DEVE SER MAIOR DO QUE ZERO.\n')
            else:
                dependente = int(input('NÚMERO DE DEPENDENTES: '))
                if(dependente < 0):
                    print(f'ERRO: O NÚMERO DE DEPENDENTES NÃO PODE SER MENOR DO QUE ZERO.\n')
                else:
                    print(f'SALÁRIO LÍQUIDO: R${lerSalario(salario, dependente)[0]: .2f}')
                    print(f'TOTAL DE DESCONTOS: R${lerSalario(salario, dependente)[1]: .2f}\n')
                    q += 1
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')