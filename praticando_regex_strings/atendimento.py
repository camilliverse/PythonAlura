import re

cpf = input('Digite seu CPF no formato (XXX.XXX.XXX-XX): ')

padrao = r'\d{3}\.\d{3}\.\d{3}-\d{2}'

if re.search(padrao, cpf):
    print('CPF está no formato correto')
else:
    print('CPF está no formato incorreto.')
