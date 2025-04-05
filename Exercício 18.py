def lerPreco (preco, reajuste, porcent):
  acrescimo = preco + (preco * porcent) / 100
  desconto = preco - (preco * porcent) / 100
  if(reajuste == 1):
    return acrescimo
  else:
    return desconto
  
q = 0
print('MENU DO PROGRAMA')
print('OPÇÕES DE REAJUSTE:')
print('OPÇÃO 1: ACRÉSCIMO')
print('OPÇÃO 2: DESCONTO')
print(f'OPÇÃO 0: PARAR O PROGRAMA\n')
while True:
  try:
    print(f'{q + 1}º MERCADORIA: ')
    reajuste = int(input('REAJUSTE: '))
    if(reajuste != 1 and reajuste != 2 and reajuste != 0):
      print('ERRO: O COMANDO DO REAJUSTE DEVE SER [1, 2 OU 0].')
    elif(reajuste == 0):
      print('FIM DO PROGRAMA!')
      break
    else:
      preco = float(input('PREÇO: '))
      if(preco <= 0):
        print('ERRO: O PREÇO DA MERCADORIA DEVE SER MAIOR DO QUE ZERO.')
      else:
        porcent = float(input('VALOR DO REAJUSTE (%): '))
        if(porcent <= 0):
          print('ERRO: O VALOR DA PORCENTAGEM DEVE SER MAIOR DO QUE ZERO.')
        else:
          print(f'PREÇO REAJUSTADO: {lerPreco (preco, reajuste,porcent): .2f}\n')
          q += 1
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')