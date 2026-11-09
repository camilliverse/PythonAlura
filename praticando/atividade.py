estudar = int(input('adicione o numero de horas que voce ira estudar: '))
academia = int(input('digite a quantidade de horas do seu treino: '))
box = int(input('digite a quantidade de horas do seu treino: '))

if(estudar >= 0 and academia >= 0 and box >= 0):
    temp_total = estudar + academia + box
    print(f'tempo total das atividades é: {temp_total} horas')
else: 
    print('erro: n pode ser negativo')