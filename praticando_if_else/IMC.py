peso = float(input('Digite sua peso: '))
altura = float(input('Digite sua altura: '))

IMC = peso / (altura**2)
print(f"Seu IMC é: {IMC}")

if IMC < 18.5: 
    print('Voce está aa baixo do peso')
elif IMC < 25:
    print('Voce está em forma')
else:
    print('Voce está acima do peso')