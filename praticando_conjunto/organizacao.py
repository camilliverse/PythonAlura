convidados = set()

while True:
    nome = input('DIgite o nome do convidado ou digite (SAIR): ')

    if nome.lower() == 'sair':
     break

    convidados.add(nome)

print(f'Convidados confirmados: {','.join(convidados)}')