distancia = float(input('Digite a distancia percorrida (em km):'))

if distancia < 100:
    print('Ira pagar R$ 10,00')
elif 100 < distancia <= 200:
    print('Ira pagar R$ 20,00')
else:
    print('Ira pagar R$ 30,00') 