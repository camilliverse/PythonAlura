
itens = ['manga', 'feijao', 'alface']

produto = input('Digite o item que vc quer verificar: ')

if produto in itens:
    print(f'Esse produto está na lista {itens}')
else:
    print('Produto não está na lista')