nomes = ['Ana', 'João', 'Pedro']
print('Lista de noomes originais: ', nomes)

digite = input('Digite o nome incorreto: ')
if digite in nomes:
    correcao = input('Digite o nome correto: ')
    posicao = nomes.index(digite)
    nomes.remove(digite)
    nomes.insert(posicao, correcao)
    print(f'O nome {digite} foi substituido pelo correto {correcao}')
    print('Lista atualizada', nomes)
else:
    print('Nome não encontrado')