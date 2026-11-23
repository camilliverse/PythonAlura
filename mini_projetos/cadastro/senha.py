import random

def gerar_senha():
    maiucuslas = 'ABCDEFGHIJKLNMOPQRSTUVWYZ'
    minusculas = 'abcdefghijklnmopqrstuvwyz'
    numeros = '0123456789'
    especiais = '!@#$%¨&*'

    senha = [random.choice(maiucuslas), random.choice(minusculas),random.choice(numeros),random.choice(especiais)]

    caracteres = minusculas + minusculas + numeros + especiais
    senha.extend(random.choices(caracteres, k=8))
    random.shuffle(senha)
    return ''.join(senha)
print('----------------------')
print(f"Senha: {gerar_senha()}")
print('----------------------')
