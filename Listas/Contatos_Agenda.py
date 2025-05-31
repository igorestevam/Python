# CRIAR / RESETAR LISTAS
agenda = []
contato = []
# FUNÇÕES
def lerNome():
  while True:
    try:
      nome = input('NOME: ')
      if(len(nome) <= 2):
        print('ERRO: INFORME UM NOME VÁLIDO.')
      else:
        break
    except:
      print('ERRO: INFORME UM NOME VÁLIDO.')
  return nome
  def lerEmail():
  while True:
    try:
      email = input('EMAIL: ')
      if(len(email) < 9):
        print('ERRO: INFORME UM EMAIL VÁLIDO')
      else:
        break
    except:
      print('ERRO: INFORME UM EMAIL VÁLIDO')
  return email
  def lerZap():
  while True:
    try:
      zap = (input('WHATSAPP (DDD + NUM): '))
      if(len(zap) < 9):
        print('ERRO: INFORME UM NÚMERO DE TELEFONE VÁLIDO.')
      else:
        break
    except:
      print('ERRO: INFORME UM NÚMERO DE TELEFONE VÁLIDO.')
  return zap
  # MAIN
while True:
  try:
    print(f'\nMENU DO PROGRAMA')
    print('OPÇÃO 1: INSERIR CONTATO')
    print('OPÇÃO 2: PESQUISAR DADOS DO CONTATO DA AGENDA PELO NOME')
    print('OPÇÃO 3: ATUALIZAR O WHATSAPP PESQUISANDO PELO EMAIL DO CONTATO')
    print('OPÇÃO 4: DELETAR UM CONTATO DA AGENDA PESQUISANDO POR NOME')
    print('QUALQUER OUTRA TECLA: FINALIZAR PROGRAMA')
    menu = int(input())
    if(menu == 1):
      print(f'\nINSERIR CONTATO')
      print(f'ENTRE COM OS DADOS DO {len(agenda) + 1}º CONTATO:')
      nome = lerNome()
      email = lerEmail()
      zap = lerZap()
      contato = [nome, email, zap]
      agenda.append(contato)
      print(f'CONTATO CADASTRADO COM SUCESSO!\n')
    elif(menu == 2):
      print(f'\nPESQUISAR DADOS DO CONTATO DA AGENDA PELO NOME')
      while True:
        try:
          nomeContato = input('NOME DO CONTATO:')
          if(len(nomeContato) <= 2):
            print('ERRO: O NOME DO CONTATO DEVE SER MAIOR.')
          else:
            break
        except:
          print('ERRO: NOME DO CONTATO.')
      listaNome = [valor[0] for valor in (agenda)]
      try:
        indice = listaNome.index(nomeContato)
        print(f'O NOME: "{nomeContato}" ESTÁ LOCALIZADO NA {indice + 1}º POSIÇÃO DA AGENDA.')
        print(f'EMAIL: {agenda[indice][1]}')
        print(f'WHATSAPP: {agenda[indice][2]}')
      except:
        print(f'O NOME: "{nomeContato}" NÃO FOI ENCONTRADO NA AGENDA.')
    elif(menu == 3):
      print(f'\nATUALIZAR O WHATSAPP PESQUISANDO PELO EMAIL DO CONTATO.')
      while True:
        try:
          emailContato = input('EMAIL DO CONTATO:')
          if(len(emailContato) < 9):
            print('ERRO: O EMAIL DO CONTATO DEVE SER MAIOR.')
          else:
              break
        except:
          print('ERRO: EMAIL NÃO ENCONTRADO.')
      try:
        print(f'NOVO NÚMERO DE WHATSAPP:')
        novoZap = input()
        if(len(novoZap) < 9):
          print('ERRO: O NÚMERO DEVE TER MAIS DE 9 DÍGITOS.')
        else:
          listaEmail = [valor[1] for valor in (agenda)]
          indice = listaEmail.index(emailContato)
          agenda[indice][2] = novoZap
          print(f'WHATSAPP DE "{agenda[indice][0]}"ATUALIZADO COM SUCESSO!')
      except:
        print('ERRO: NÃO FOI POSSÍVEL ATUALIZAR O CADASTRO.')
    elif(menu == 4):
      print(f'\nDELETAR CONTATO DA AGENDA PESQUISANDO POR NOME.')
      while True:
        try:
          nomeContato = input('NOME DO CONTATO: ')
          if(len(nomeContato) <= 2):
            print('ERRO: O NOME DO CONTATO DEVE SER MAIOR.')
          else:
            break
        except:
          print('ERRO: NOME DO CONTATO NÃO ENCONTRADO')
      try:
        listaNome = [valor[0] for valor in (agenda)]
        indice = listaNome.index(nomeContato)
        agenda.remove([nomeContato, agenda[indice][1], agenda[indice][2]])
        print(f'O CONTATO {nomeContato} FOI REMOVIDO COM SUCESSO!')
      except:
        print('ERRO: REMOÇÃO DO CONTATO')
    else:
      print(f'FIM DAS OPERAÇÕES!')
      break
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
    break
