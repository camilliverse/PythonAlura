vendas = input('Por favor, digite o valor das vendas: ').split()
total = sum(map(float, vendas))
print(f'O total de vendas foi: {total}')