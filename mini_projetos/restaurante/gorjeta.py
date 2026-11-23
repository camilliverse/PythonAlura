#gorjeta = pocentagem / 100 * conta

def gorjeta():
    conta = float(input('digite o valor da conta: '))
    porcentagem_gorjeta = float(input('digite a porcentagem de gorjetas: '))
    gorjeta = (porcentagem_gorjeta / 100) * conta
    total = conta + gorjeta

    print(f'valor da gorjeta: R$ {gorjeta:.2f}')
    print(f'total a pagar: R$ {total:.2f}')
