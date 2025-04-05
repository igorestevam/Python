def calculadora (n1, n2, operador):
  operacao = 0
  if(operador == 1):
    operacao = n1 + n2
    return operacao
  elif(operador == 2):
    operacao = n1 - n2
    return operacao
  elif(operador == 3):
    operacao = n1 * n2
    return operacao
  elif(operador == 4):
    operacao = n1 / n2
    return operacao
  elif(operador == 5):
    operacao = n1 % n2
    return operacao
  else:
    operacao = n1 // n2
    return operacao
  
print('MENU DO PROGRAMA:')
print('OPÇÃO 1: SOMA')
print('OPÇÃO 2: SUBTRAÇÃO')
print('OPÇÃO 3: MULTIPLICAÇÃO')
print('OPÇÃO 4: DIVISÃO')
print('OPÇÃO 5: MOD')
print(f'OPÇÃO 6: DIV\n')
q = 0
while(q < 7):
  try:
    print(f'{q + 1}º OPERAÇÃO')
    print('INFORME 2 NÚMEROS INTEIROS:')
    n1 = int(input('1º NÚMERO: '))
    n2 = int(input('2º NÚMERO: '))
    operador = int(input('INFORME O OPERADOR: '))
    if(operador < 1 or operador > 6):
      print(f'ERRO: O OPERADOR SÓ PODE SER INFORMADO POR [1, 2, 3, 4, 5 OU 6].\n')
    else:
      resultado = calculadora (n1, n2, operador)
      if(operador == 1):
        print(f'{n1} + {n2} = {resultado}\n')
      elif(operador == 2):
        print(f'{n1} - {n2} = {resultado}\n')
      elif(operador == 3):
        print(f'{n1} * {n2} = {resultado}\n')
      elif(operador == 4):
        print(f'{n1} / {n2} = {resultado: .2f}\n')
      elif(operador == 5):
        print(f'{n1} % {n2} = {resultado}\n')
      else:
        print(f'{n1} // {n2} = {resultado}\n')
      q += 1
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')