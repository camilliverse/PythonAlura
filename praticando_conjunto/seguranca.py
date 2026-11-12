permissoes_principais = set(p.strip() for p in input('Permissoções principais: ').lower().split(','))
#lower = transforma tudo em minuscula | .split adiciona , em todos os campos digitados | for p in percorre todos os itens da lista
#p.strip remove espaçõs do incio ao fim.
permissoes_solicitadas = set(p.strip() for p in input('Permissoções solicitadas: ').lower().split(','))

subconjunto = permissoes_solicitadas.issubset(permissoes_principais)

if subconjunto:
    print(f'Permissoes solicitadas fazem parte das permissoes principais {permissoes_principais}')
else:
    print('As permissoes que voce deseja não fazem parte das permissoes principais.')

