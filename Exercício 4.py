def lerAno (ano):
  if((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0):
    return 1
  else:
    return 0

q = 0
while(q < 5):
  try:
    print('INFORME UM ANO:')
    ano = int(input(f'{q + 1}º ANO: '))
    if(ano <= 0):
      print('ERRO: O VALOR DO ANO DEVE SER MAIOR DO QUE ZERO.\n')
    else:
      if(lerAno(ano) == 1):
        print(f'O ANO {ano} É BISSEXTO.\n')
      else:
        print(f'O ANO {ano} NÃO É BISSEXTO.\n')
      q += 1
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')