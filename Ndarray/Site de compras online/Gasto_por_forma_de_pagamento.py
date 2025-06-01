# MÍNIMO, MÁXIMO E MÉDIA DOS GASTOR POR FORMA DE PAGAMENTO (DÉBITO E CRÉDITO)
debito = dataset3[dataset3[:,3] == 0]
credito = dataset3[dataset3[:,3] == 1]
print(f'DADOS DOS {debito.shape[0]} CLIENTES QUE PAGARAM NO DÉBITO: ')
print(f'MENOR GASTO: R${np.min(debito[:,1]): .2f}')
print(f'MAIOR GASTO: R${np.max(debito[:,1]): .2f}')
print(f'MÉDIA DE GASTOS: R${np.mean(debito[:,1]): .2f}')
print(f'\nDADOS DOS {credito.shape[0]} CLIENTES QUE PAGARAM NO CRÉDITO: ')
print(f'MENOR GASTO: R${np.min(credito[:,1]): .2f}')
print(f'MAIOR GASTO: R${np.max(credito[:,1]): .2f}')
print(f'MÉDIA DE GASTOS: R${np.mean(credito[:,1]): .2f}')
