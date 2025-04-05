def multiplicacao (n, opcao):
  par = 1
  impar = 1
  if(opcao == 1):
    for cont in range (1, n + 1):
      if(cont % 2 != 0):
        impar *= cont
    return impar
  else:
    for cont in range (1, n + 1):
      if(cont % 2 == 0):
        par *= cont
    return par
  
q = 0
while(q < 5):
  try:
    print('INFORME UM NÚMERO INTEIRO MAIOR QUE ZERO: ')
    n = int(input(f'{q + 1}º NÚMERO: '))
    if(n <= 0):
      print('ERRO: O NÚMERO INFORMADO DEVE SER MAIOR DO QUE ZERO')
    else:
      print('OPÇÕES DE MULTIPLICAÇÃO [1 = ÍMPAR, 2 = PAR]: ')
      opcao = int(input(f'{q + 1}º OPÇÃO: '))
      if(opcao != 1 and opcao != 2):
        print('ERRO: A OPÇÃO DEVE SER INFORMADA APENAS POR 1 OU 2.')
      elif(n == 1 and opcao == 2):
        print('NÃO EXISTE NÚMEROS PARES ENTRE [1, 1].')
      else:
        if(opcao == 1):
          multImpar = multiplicacao (n, 1)
          print(f'A MÚLTIPLICAÇÃO DOS ÍMPARES ENTRE [1, {n}] É: {multImpar}\n')
        else:
          multPar = multiplicacao (n, 2)
          print(f'A MULTIPLICAÇÃO DOS PARES ENTRE [1, {n}] É: {multPar}\n')
        q += 1
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')