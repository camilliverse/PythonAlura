produtos = {}

for i in range(3):
    nome = input('Inserir nome do produto: ')
    quantidade = int(input('Digite a quantidade: '))

    produtos[nome] = quantidade

print(f'Dicionario de produtos: {produtos}')