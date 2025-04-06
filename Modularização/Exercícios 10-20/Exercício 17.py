# FUNÇÃO
def lerJogo(valor, crianca, jovem, adulto, doador):
    
    valorTotal = jovem * (valor / 2) + adulto * valor + doador * (valor / 2)
    publico = crianca + jovem + adulto + doador
    return publico, valorTotal
# PRINCIPAL
q = 0
while True:
    try:
        print('MENU DO PROGRAMA:')
        print('OPÇÃO 1: INICIAR.')
        print('QUALQUER OUTRA TECLA: FINALIZAR')
        menu = int(input())
        if(menu != 1):
            print(f'FIM DO PROGRAMA!')
            break
        else:
            print(f'{q + 1}º JOGO: ')
            valor = float(input('VALOR DO INGRESSO: '))
            if(valor <= 0):
                print(f'ERRO: O VALOR DO INGRESSO DEVE SER MAIOR DO QUE 0.\n')
            else:
                crianca = int(input('QUANTIDADE DE CRIANÇAS: '))
                jovem = int(input('QUANTIDADE DE JOVENS: '))
                adulto = int(input('QUANTIDADE DE ADULTOS (NÃO DOADORES): '))
                doador = int(input('QUANTIDADE DE ADULTOS (DOADORES): '))
                if(crianca < 0 or jovem < 0 or adulto < 0 or doador < 0):
                    print(f'ERRO: A QUANTIDADE DE UM PÚBLICO NÃO PODE SER MENOR DO QUE ZERO.\n')
                else:
                    print(f'PÚBLICO TOTAL: {lerJogo(valor, crianca, jovem, adulto, doador)[0]} PESSOAS.')
                    print(f'VALOR TOTAL ARRECADADO: R${lerJogo(valor, crianca, jovem, adulto, doador)[1]}\n')
                    q += 1
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')