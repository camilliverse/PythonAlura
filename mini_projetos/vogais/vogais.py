def contar_vogais(texto):
    vogais = 'aeiou'
    quantidade = 0 

    for letra in texto.lower():
        if letra in vogais:
            quantidade += 1 

    return quantidade

texto = input('digite um texto: ')
print(f'o texto contem {contar_vogais(texto)} vogais.')