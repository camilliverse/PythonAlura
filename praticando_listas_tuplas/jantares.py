lista = ['Pikachu', 'Infernap', 'Greninja']

print(f'Lista atual {lista}')

nome = input('Digite o nome do novo convidado: ')
posicao= input('Digite a posicao na qual deseja inserir os convidados: ')

lista.insert(int(posicao) - 1, nome)
print(f'Lista atualizada de {lista}')