import random

def numero():
    numero_computador = random.choice(1, 100)
    tentativas = 0

    while True:
        try:
            usuario = int(input('Tente adivinhar o numero de 1 a 100: '))

            if not 1 <= usuario <= 100:
                raise ValueError('numero fora de 1 a 100, por favor digite um numero valido')

            tentativas += 1

            if usuario < numero_computador:
                print('muito baixo, tente novamente')
            elif usuario > numero_computador:
                print('muito alto, tente novamente')
            else:
                print('parabens voce ganho')
            break

        except ValueError as e:
            print(f'entrada invalida {e}')

    numero()