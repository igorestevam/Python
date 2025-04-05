import math
def i (raio):
  area = math.pi * (raio ** 2)
  return area
def ii (raio, altura):
  volume = i (raio) * altura
  return volume

try:
  raio = float(input('INFORME O RAIO DO CILINDRO: '))
  if(raio <= 0):
    print('ERRO: O VALOR DO RAIO DEVE SER MAIOR DO QUE ZERO.')
  else:
    altura = float(input('INFORME A ALTURA DO CILINDRO: '))
    if(altura <= 0):
      print('ERRO: O VALOR DA ALTURA DEVE SER MAIOR DO QUE ZERO.')
    else:
      print(f'ÁREA DO CÍRCULO DO CILINDRO: {i(raio): .2f}')
      print(f'VOLUME DO CILINDRO: {ii(raio, altura): .2f}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')