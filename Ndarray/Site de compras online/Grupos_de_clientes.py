# SEPARAR CLIENTES POR GRUPOS
# QUANTIDADE DE CLIENTES BRONZE (GASTARAM, ATÉ R$100,00)
indexBronze = dataset3[:,1] <= 100.00
bronze = sum(indexBronze)
# QUANTIDADE DE CLIENTES PRATA (GASTARAM ATÉ R$500 REAIS)
indexPrata = dataset3[:,1] <= 500.00
prata = sum(indexPrata) - bronze
# QUANTIDADE DE CLIENTES OURO (GASTARAM ATÉ R$1000,00)
indexOuro = dataset3[:,1] <= 1000.00
ouro = sum(indexOuro) - sum(indexPrata)
# QUANTIDADE DE CLIENTES DIAMANTE (GASTARAM MAIS DE R$1000,00)
indexDiamante = dataset3[:,1] > 1000
diamante = sum(indexDiamante)
print('QUANTIDADE ABSOLUTA DE CLIENTES POR CARTÃO:')
print(f'BRONZE: {bronze} CLIENTE(S)')
print(f'PRATA: {prata} CLIENTE(S)')
print(f'OURO: {ouro} CLIENTE(S)')
print(f'DIAMANTE: {diamante} CLIENTE(S)\n')
print('QUANTIDADE RELATIVA (%) DE CLIENTES POR CARTÃO:')
print(f'BRONZE:{(bronze / len(dataset3[:,1])) * 100: .1f}% DOS CLIENTE(S)')
print(f'PRATA:{(prata / len(dataset3[:,1])) * 100: .1f}% DOS CLIENTE(S)')
print(f'OURO:{(ouro / len(dataset3[:,1])) * 100: .1f}% DOS CLIENTE(S)')
print(f'DIAMANTE:{(diamante / len(dataset3[:,1])) * 100: .1f}% DOS CLIENTE(S)\n')
# TODOS OS CLIENTES RECEBEM UM CARTÃO FIDELIDADE QUE CUSTA R$3,87 PARA SER CONFECCIONADO
print('CUSTO DE CONFECÇÃO DOS CARTÕES POR GRUPO: ')
print(f'BRONZE: R${bronze * 3.87: .2f}')
print(f'PRATA: R${prata * 3.87: .2f}')
print(f'OURO: R${ouro * 3.87: .2f}')
print(f'DIAMANTE: R${diamante * 3.87: .2f}\n')
print(f'CUSTO TOTAL DA CONFECÇÃO DOS CARTÕES: R${len(dataset3[:,1]) * 3.87: .2f}')
