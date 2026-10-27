import os

informacao_pessoal = [[
{'nome': 'Jose', 'idade': 30, 'cidade': 'Belem'} ]]

print(informacao_pessoal)

informacao_pessoal['idade'] = 21

informacao_pessoal['profissao'] = 'Pescador'

del informacao_pessoal['cidade']

print()
print(informacao_pessoal)

quadros = []

for numero in range(1, 6):
    quadros[numero] = numero ** 2 

print(quadros)