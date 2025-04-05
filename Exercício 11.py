def lerAno (ano, n):
  quo = 0
  res = 0
  bi = 0
  if((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0):
    bi = 1
  else:
    bi = 0
  if(n == 4):
    quo = ano // 4
    res = ano % 4
  elif(n == 100):
    quo = ano // 100
    res = ano % 100
  else:
    quo = ano // 400
    res = ano % 400
  return bi, quo, res

try:
  ano = int(input('INFORME UM ANO QUALQUER: '))
  if(ano <= 0):
    print('ERRO: O ANO INFORMADO DEVE SER MAIOR DO QUE ZERO')
  else:
    n = int(input('INFORME QUAL NÚMERO DIVIDIRÁ O ANO [4, 100 OU 400]: '))
    if(n != 4 and n != 100 and n != 400):
      print('ERRO: O NÚMERO INFORMADO DEVE SER [4, 100 OU 400].')
    else:
      bissexto = lerAno(ano, n) [0]
      quociente = lerAno(ano, n) [1]
      resto = lerAno(ano, n) [2]
      if(bissexto == 1):
        print(f'O ANO {ano} É BISSEXTO')
      else:
        print(f'O ANO {ano} NÃO É BISSEXTO')
      print(f'QUOCIENTE DA DIVISÃO: {quociente}')
      print(f'RESTO DA DIVISÃO: {resto}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')