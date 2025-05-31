# CRIAR/RESETAR
import numpy
empresa = []
funcionario = []
# FUNÇÕES
def lerNome():
  while True:
    try:
      nome = input('NOME: ')
      if(len(nome) < 2):
        print('ERRO: O NOME DEVE SER MAIOR.')
      else:
        break
    except:
      print('ERRO: INFORME UM NOME VÁLIDO')
  return nome
def lerCargo():
  while True:
    try:
      cargo = int(input('CARGO [1, 2, 3 OU 4]: '))
      if(cargo < 1 or cargo > 4):
        print('ERRO: O CARGO DEVE SER INFORMADO POR [1, 2, 3 OU 4].')
      else:
        break
    except:
      print('ERRO: INFORME UM CARGO VÁLIDO')
  return cargo
def lerMat():
  mean = 10000
  std = 1000
  size = 1
  mat = [valor for valor in (numpy.random.normal(mean, std, size))]
  return mat
def lerPlano():
  while True:
    try:
      plano = int(input('POSSUI PLANO DE SAÚDE [1 = SIM, 0 = NÃO]: '))
      if(plano < 0 or plano > 1):
        print('ERRO: O PLANO DEVE SER INFORMADO PELOS DÍGITOS 1 OU 0.')
      else:
        break
    except:
      print('ERRO: INFORME UM DÍGITO VÁLIDO')
  return plano
def lerSalario():
  while True:
    try:
      salario = float(input('SALÁRIO: '))
      if(salario <= 0):
        print('ERRO: O SALÁRIO NÃO PODE SER MENOR DO QUE ZERO.')
      else:
        break
    except:
      print('ERRO: INFORME UM SALÁRIO VÁLIDO')
  return salario
# MAIN
while True:
  try:
    print(f'\nMENU DO PROGRAMA')
    print('OPÇÃO 1: CADASTRAR FUNCIONÁRIO')
    print('OPÇÃO 2: EXIBIR TAXA DE ADESÃO (%) AO PLANO DE SAÚDE')
    print('OPÇÃO 3: EXIBIR NOMES DOS FUNCIONÁRIOS QUE POSSUEM PLANO DE SAÚDE')
    print('OPÇÃO 4: EXIBIR CARGOS DOS FUNCIONÁRIOS QUE ESTÃO ACIMA DA MÉDIA SALARIAL')
    print('OPÇÃO 5: EXIBIR O TOTAL DA FOLHA DE PAGAMENTO (BRUTO E LÍQUIDO)')
    print('QUALQUER TECLA: ENCERRAR O PROGRAMA')
    menu = int(input())
    if(menu < 1 or menu > 5):
      print('FIM DO PROGRAMA!')
      break
    elif(menu == 1):
      if(len(empresa) < 6):
        print(f'\nCADASTRO DE FUNCIONÁRIOS:')
        print(f'INSIRA OS DADOS DO {len(empresa) + 1}º FUNCIONÁRIO:')
        nome = lerNome()
        cargo = lerCargo()
        mat = lerMat()
        plano = lerPlano()
        salario = lerSalario()
        funcionario = [nome, cargo, mat, plano, salario]
        empresa.append(funcionario)
        print(f'\nFUNCIONÁRIO CADASTRADO COM SUCESSO!')
      else:
        print('O NÚMERO MÁXIMO DE CADASTROS DE FUNCIONÁRIOS FOI ATINGIDO!')
    elif(menu == 2):
      print(f'\nTAXA DE ADESÃO (%) AO PLANO DE SAÚDE:')
      try:
        total = sum(valor[3] for valor in empresa)
        print(f'{(total / len(empresa)) * 100: .2f}% DOS FUNCIONÁRIOS ADERIRAM AO PLANO DE SAÚDE.')
      except:
        print('ERRO: NÃO HÁ FUNCIONÁRIOS CADASTRADOS.')
    elif(menu == 3):
      try:
        print(f'\nNOME DOS FUNCIONÁRIOS QUE POSSUEM PLANO DE SAÚDE:')
        funcPlano = [valor for valor in empresa if(valor[3] == 1)]
        for valor in funcPlano:
          print(f'NOME: {valor[0]}')
      except:
        print('ERRO: NENHUM FUNCIONÁRIO POSSUI PLANO DE SAÚDE')
    elif(menu == 4):
      q = 0
      print(f'\nCARGOS DOS FUNCIONÁRIOS ACIMA DA MÉDIA:')
      try:
        media = sum([valor[4] for valor in empresa]) / len(empresa)
        acimaMedia = [valor for valor in empresa if(valor[4] > media)]
        for valor in acimaMedia:
          print(f'CARGO DO {q + 1}º FUNCIONÁRIO: {valor[1]}')
          q += 1
      except:
        print('ERRO: NÃO HÁ FUNCIONÁRIOS CADASTRADOS')
    else:
      try:
        print(f'\nTOTAIS BRUTO E LÍQUIDO DA FOLHA DE PAGAMENTO:')
        bruto = sum([valor[4] for valor in empresa])
        liquido = bruto - 212.54 * sum(valor[3] for valor in empresa)
        print(f'BRUTO: {bruto: .2f}')
        print(f'LÍQUIDO: {liquido: .2f}')
      except:
        print('ERRO: NÃO HÁ FUNCIONÁRIOS CADASTRADOS')
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
