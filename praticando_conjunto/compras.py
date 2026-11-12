laura = set(input('Laura digite suas compras: ').split(','))
ana = set(input('Ana digite suas compras compras: ').split(','))

comuns = laura.intersection(ana)

exclusivo_laura = laura.difference(ana)
exclusivo_ana = ana.difference(laura)

print(f'Itens em comun: {comuns}')
print(f'Compras laura: {exclusivo_laura}')
print(f'Compras Ana: {exclusivo_ana}')
