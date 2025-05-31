# CRIAR/RESETAR
import numpy
banco = []
correntista = []
extrato = []
# FUNÇÕES
def lerNome():
  while True:
    try:
      nome = input('NOME: ')
      if(len(nome) < 2):
        print('ERRO: O NOME NÃO PODE TER MENOS DE DUAS LETRAS.')
      else:
        break
    except:
      print('ERRO: INFORME UM NOME VÁLIDO.')
  return nome
  def lerConta():
  while True:
    try:
      conta = int(input('NÚMERO DA CONTA: '))
      if(conta >= 100000 or conta <= 0):
        print('ERRO: O NÚMERO DA CONTA DEVE SER MENOR QUE [100.000].')
      else:
        break
    except:
      print('ERRO: INFORME UM NÚMERO DA CONTA VÁLIDO')
  return conta
  #MAIN
while True:
  try:
    print(f'\nMENU DO PROGRAMA')
    print('OPÇÃO 1: INSERIR CONTATO')
    print('OPÇÃO 2: CORRENTISTA COM A MAIOR MOVIMENTAÇÃO ANUAL DE EXTRATO')
    print('OPÇÃO 3: MOVIMENTAÇÃO FINANCEIRA TOTAL POR TRIMESTRE PESQUISANDO PELA CONTA')
    print('OPÇÃO 4: RELATÓRIO FINANCEIRO COM A MOVIMENTAÇÃO ANUAL DE TODOS OS CORRENTISTAS')
    print('OPÇÃO 5: LUCRO DOS ACIONISTAS')
    print('QUALQUER TECLA: SAIR')
    menu = int(input())
    # INSERÇÃO DE CONTATO
    if(menu == 1):
      print(f'\nINSERIR CONTATO: ')
      print(f'ENTRE COM OS DADOS DO {len(banco) + 1}º CORRENTISTA: ')
      nome = lerNome()
      conta = lerConta()
      # GERANDO EXTRATOS ALETÓRIOS PARA OS 12 MESES
      mean = 5000.01
      std = 505.01
      size = 12 # meses
      extrato = [valor for valor in (numpy.random.normal(mean, std, size))]
      correntista = [nome, conta, extrato]
      banco.append(correntista)
      print('CORRENTISTA CADASTRADO COM SUCESSO!')
    # RELATÓRIO 1: CORRENTISTA COM A MAIOR MOVIMENTAÇÃO ANUAL DE EXTRATO
    elif(menu == 2):
      if(len(banco) == 0):
        print('ERRO: NÃO HÁ CORRENTISTAS CADASTRADOS.')
      else:
        total = [sum(valor[2]) for valor in banco]
        maxTotal = max(total)
        maxIndice = total.index(maxTotal)
        print(f'\nDADOS DO CORRENTISTA COM A MAIOR MOVIMENTAÇÃO DO ANO:')
        print(f'NOME: {banco[maxIndice][0]}')
        print(f'CONTA: {banco[maxIndice][1]}')
    # RELATÓRIO 2: VER A MOVIMENTAÇÃO ANUAL TOTAL DO CORRENTISTA
    elif(menu == 3):
      print(f'\nMOVIMENTAÇÃO TOTAL POR TRIMESTRE DE UM CORRENTISTA PESQUISANDO SUA CONTA:')
      while True:
        try:
          contaCorrentista = int(input('NÚMERO DA CONTA: '))
          if(contaCorrentista >= 100000 or conta <= 0):
            print('ERRO: O NÚMERO DA CONTA DEVE SER MENOR QUE [100.000].')
          else:
            break
        except:
          print('ERRO: INFORME UM NÚMERO DA CONTA VÁLIDO')
      listaCorrentista = [valor[1] for valor in banco]
      try:
        indice = listaCorrentista.index(contaCorrentista)
        print(f'MOVIMENTAÇÃO DO PRIMEIRO TRIMESTRE: R${sum(banco[indice][2][0:3]): .2f}')
        print(f'MOVIMENTAÇÃO DO SEGUNDO TRIMESTRE: R${sum(banco[indice][2][3:6]): .2f}')
        print(f'MOVIMENTAÇÃO DO TERCEIRO TRIMESTRE: R${sum(banco[indice][2][6:9]): .2f}')
        print(f'MOVIMENTAÇÃO DO QUARTO TRIMESTRE: R${sum(banco[indice][2][9:12]): .2f}')
      except:
        print(f'ERRO: O NÚMERO DA CONTA "{contaCorrentista}" NÃO FOI ENCONTRADO NO BANCO.')
    # RELATÓRIO 3: RELATÓRIO FINANCEIRO COM A MOVIMENTAÇÃO ANUAL DE TODOS OS CORRENTISTAS
    elif(menu == 4):
      try:
        total = [sum(valor[2]) for valor in banco]
        print(f'\nMOVIMENTAÇÃO ANUAL DE TODOS OS CORRENTISTAS: R${sum(total): .2f}')
      except:
        print('ERRO: NÃO HÁ CORRENTISTAS CADASTRADOS.')
    # RELATÓRIO 4: LUCRO DOS ACIONISTAS
    elif(menu == 5):
      try:
        total = [sum(valor[2]) for valor in banco]
        print(f'LUCRO DOS ACIONISTAS: R${sum(total) * 0.07: .2f}')
      except:
        print('ERRO: NÃO HÁ CORRENTISTAS CADASTRADOS.')
    else:
      print('FIM DO PROGRAMA!')
      break
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
