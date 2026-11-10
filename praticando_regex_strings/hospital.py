import re 

paciente = input('Digite o nome completo e o ano de nascimento do paciente: ')
padrao = r'(\w+) (\w+) - (\d{4})'

resultado = re.search(padrao, paciente)

if resultado: 
    primeiro_nome = resultado.group(1)
    sobrenome = resultado.group(2)
    ano = resultado.group(3)

    print(f'Primeiro nome {primeiro_nome}')
    print(f'Sobrenome {sobrenome}')
    print(f'Ano de Nascimento: {ano}')
else:
    print('Formato invalido!')