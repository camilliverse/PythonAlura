textoone = set(input('Texto 1 : ').lower().split())
texttwo = set(input('Texto 2 : ').lower().split())

comun = textoone.intersection(texttwo)
print(textoone)
print(texttwo)
print(f'Palavras em comun: {comun}')