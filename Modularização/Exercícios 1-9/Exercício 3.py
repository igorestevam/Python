import math
def f1 (n, p):
  arranjo = math.factorial(n) / math.factorial(n - p)
  return arranjo
def f2 (n, p):
  combinacao = f1(n, p) / math.factorial(p)
  return combinacao

q = 0
while True:
  print('INFORME DOIS NÚMEROS INTEIROS MAIORES DO QUE ZERO:')
  try:
    n = int(input(f'{q + 1}º NÚMERO n: '))
    if(n < 0):
      print('FIM DO PROGRAMA!')
      break
    else:
      p = int(input(f'{q + 1}º NÚMERO p: '))
      if(p < 0 or p > n):
        print('FIM DO PROGRAMA!')
        break
      else:
        print(f'ARRANJO DE {n} ELEMENTOS COMBINADOS {p} A {p} = {f1(n, p)}')
        print(f'COMBINAÇÃO DE {n} ELEMENTOS COMBINADOS {p} A {p} = {f2(n, p)}\n')
        q += 1
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')