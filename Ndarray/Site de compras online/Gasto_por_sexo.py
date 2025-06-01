# MÍNIMO, MÁXIMO E MÉDIA DOS GASTOS DE HOMENS E MULHERES
homem = dataset3[dataset3[:,2] == 1]
mulher = dataset3[dataset3[:,2] == 0]
print(f'DADOS DOS {homem.shape[0]} CLIENTES HOMENS: ')
print(f'MENOR GASTO: R${np.min(homem[:,1]): .2f}')
print(f'MAIOR GASTO: R${np.max(homem[:,1]): .2f}')
print(f'MÉDIA DE GASTOS: R${np.mean(homem[:,1]): .2f}')
print(f'\nDADOS DAS {mulher.shape[0]} CLIENTES MULHERES: ')
print(f'MENOR GASTO: R${np.min(mulher[:,1]): .2f}')
print(f'MAIOR GASTO: R${np.max(mulher[:,1]): .2f}')
print(f'MÉDIA DE GASTOS: R${np.mean(mulher[:,1]): .2f}')
