# FUNÇÃO
def lerPreco (preco, reajuste):
    total = preco + preco * (reajuste / 100)
    return total
# PRINCIPAL
q = 0
while(q < 5):
    try:
        print(f'{q + 1}º MERCADORIA: ')
        preco = float(input('PREÇO (R$): '))
        if(preco <= 0):
            print(f'ERRO: O PREÇO INFORMADO DEVE SER MAIOR DO QUE ZERO.')
        else:
            reajuste = float(input('REAJUSTE (%): '))
            if(reajuste < 0):
                print(f'ERRO: O REAJUSTE NÃO PODE SER MENOR DO QUE ZERO.')
            else:
                print(f'PREÇO REAJUSTADO: R${lerPreco(preco, reajuste): .2f}')
                print(f'VALOR DO REAJUSTE: R${lerPreco(preco, reajuste) - preco: .2f}')
                q += 1
    except Exception as ERRO_EXCECAO:
        print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')