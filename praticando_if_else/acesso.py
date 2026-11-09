horario = int(input('Digite a hora atual (formato 24 horas): '))

if 8 <= horario < 18: 
    print('Acesso permitido')
else:
    print('Acesso negado')