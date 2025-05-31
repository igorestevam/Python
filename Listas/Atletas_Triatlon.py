# CRIAR/ RESETAR
triatlon = []
atleta = []
dataNasc = []
tempo = []
# FUNÇÕES
def lerNome():
  while True:
    try:
      nome = input('NOME: ')
      if(len(nome) < 2):
        print('ERRO: INFORME UM NOME MAIOR.')
      else:
        break
    except:
      print('ERRO: INFORME UM NOME VÁLIDO')
  return nome
  def lerPatrocinador():
  while True:
    try:
      patrocinador = int(input('PATROCINADOR (1 = redbull, 2 =monster, 3 = tnt): '))
      if(patrocinador < 1 or patrocinador > 3):
        print('ERRO: O DÍGITO PARA INFORMAR O PATROCINADOR DEVE SER DE 1 À 3.')
      else:
        break
    except:
      print('ERRO: INFORME UM PATROCINADOR VÁLIDO.')
  return patrocinador
  def lerData():
  print('DATA DE NASCIMENTO: ')
  while True:
    try:
      dia = int(input('DIA: '))
      if(dia < 1 or dia > 31):
        print('ERRO: O DIA DEVE ESTAR ENTRE [1 E 31].')
      else:
        mes = int(input('MÊS: '))
        if(mes < 1 or mes > 12):
          print('ERRO: O MÊS DEVE ESTAR ENTRE [1 E 12].')
        else:
          ano = int(input('ANO: '))
          if(ano < 1900 or ano > 2025):
            print('ERRO: INFORME UM ANO VÁLIDO.')
          else:
            break
    except:
      print('ERRO: INFORME UMA DATA DE NASCIMENTO VÁLIDA')
  return dia, mes, ano
  def lerTempo():
  print('TEMPO DE CADA ETAPA DO TRIATLON (SEGUNDOS): ')
  while True:
    try:
      natacao = int(input('NATAÇÃO: '))
      if(natacao <= 0):
        print('ERRO: O TEMPO EM SEGUNDOS DEVE SER MAIOR DO QUE ZERO.')
      else:
        corrida = int(input('CORRIDA: '))
        if(corrida <= 0):
          print('ERRO: O TEMPO EM SEGUNDOS DEVE SER MAIOR DO QUE ZERO.')
        else:
          ciclismo = int(input('CICLISMO: '))
          if(ciclismo <= 0):
            print('ERRO: O TEMPO EM SEGUNDOS DEVE SER MAIOR DO QUE ZERO.')
          else:
            break
    except:
      print('ERRO: TEMPO EM SEGUNDOS INVÁLIDO.')
  return natacao, corrida, ciclismo
  # MAIN
while True:
  try:
    print(f'\nMENU DO PROGRAMA:')
    print('OPÇÃO 1: CADASTRAR ATLETA')
    print('OPÇÃO 2: EXIBIR NOMES DOS TRIATLETAS COM OS MELHORES TEMPOS EM CADA ETAPA')
    print('OPÇÃO 3: EXIBIR NOMES E PATROCINADORES DO MELHOR ATLETA')
    print('OPÇÃO 4: EXIBIR NOME E TEMPO DOS ATLETAS QUE FIZERAM UM TEMPO ABAIXO DA MÉDIA')
    print('QUALQUER TECLAA: ENCERRAR PROGRAMA')
    menu = int(input())
    if(menu < 1 or menu > 4):
      print(f'\nFIM DO PROGRAMA!')
      break
    elif(menu == 1):
      print(f'\nOPÇÃO 1: CADASTRAR ATLETA')
      print(f'CADASTRO DO {len(triatlon) + 1}º ATLETA: ')
      try:
        nome = lerNome()
        patrocinador = lerPatrocinador()
        dataNasc = lerData()
        tempo = lerTempo()
        atleta = [nome, patrocinador, dataNasc, tempo]
        triatlon.append(atleta)
        print(f'\nATLETA CADASTRADO COM SUCESSO!')
      except:
        print('ERRO: CADASTRO DO ATLETA.')
    elif(menu == 2):
      print(f'\nOPÇÃO 2: EXIBIR NOMES DOS TRIATLETAS COM OS MELHORES TEMPOS EM CADA ETAPA')
      try:
        # MAX NATAÇÃO
        listaNat = [valor[3][0] for valor in triatlon]
        minNat = min(listaNat)
        indiceNat = listaNat.index(minNat)
        # MAX CORRIDA
        listaCor = [valor[3][1] for valor in triatlon]
        minCor = min(listaCor)
        indiceCor = listaCor.index(minCor)
        # MAX CICLISMO
        listaCic = [valor[3][2] for valor in triatlon]
        minCic = min(listaCic)
        indiceCic = listaCic.index(minCic)
        print(f'MELHOR TEMPO DE NATAÇÃO: {triatlon[indiceNat][0]} segundos')
        print(f'MELHOR TEMPO DE CORRIDA: {triatlon[indiceCor][0]} segundos')
        print(f'MELHOR TEMPO DE CICLISMO: {triatlon[indiceCic][0]} segundos')
      except:
        print('ERRO: NENHUM ATLETA CADASTRADO.')
    elif(menu == 3):
      print(f'\nOPÇÃO 3: EXIBIR NOMES E PATROCINADORES DO MELHOR ATLETA')
      try:
        total = [sum(valor[3]) for valor in triatlon]
        minTotal = min(total)
        indice = total.index(minTotal)
        print(f'NOME: {triatlon[indice][0]}')
        print(f'PATROCINADOR: {triatlon[indice][1]}')
      except:
        print('ERRO: NENHUM ATLETA CADASTRADO.')
    else:
      print(f'\nOPÇÃO 4: EXIBIR NOME E TEMPO DOS ATLETAS QUE FIZERAM UM TEMPO ABAIXO DA MÉDIA')
      try:
        total = [sum(valor[3]) for valor in triatlon]
        media = sum(total) / len(triatlon)
        abaixoMedia = [valor for valor in triatlon if(sum(valor[3]) < media)]
        for valor in abaixoMedia:
          print(f'NOME: {valor[0]}\nTEMPO:{sum(valor[3])} segundos\n')
      except:
        print('ERRO: NENHUM ATLETA CADASTRADO.')
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
