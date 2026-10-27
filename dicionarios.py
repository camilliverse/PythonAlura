informacao_pessoal = {
    'nome': 'Jose',
    'idade': 30,
    'cidade': 'Belem'
}

print(informacao_pessoal)

# Alterar idade
informacao_pessoal['idade'] = 21

# Adicionar profissão
informacao_pessoal['profissao'] = 'Pescador'

# Remover cidade
del informacao_pessoal['cidade']

print(informacao_pessoal)

# Exercício 3
quadros = {}

for numero in range(1, 6):
    quadros[numero] = numero ** 2

print(quadros)

# Exercício 4
if "idade" in informacao_pessoal:
    print("A chave existe!")
else:
    print("A chave não existe!")