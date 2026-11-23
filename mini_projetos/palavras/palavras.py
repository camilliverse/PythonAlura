texto = input('digite um texto: ')

palavras_longa = []

for palavra in texto.split():
    if len(palavra) > 10:
        palavras_longa.append(palavra)

if palavras_longa:
    print('palavras longas encontradas:')
    for palavras in palavras_longa:
        print(palavra)
else:
    print('nenhuma palavra longa foi encontrada.')
