voluntatios = []

while True:
    nome = input("Digite o nome do voluntário (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    voluntatios.append(nome)

print('\nVoluntarios registrados: ' , voluntatios)