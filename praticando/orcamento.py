orçamento = float(input('Digite o total de dispesas do mes (R$): '))

limite = 3000

if orçamento > limite: 
    print('ATENÇÃO: Voce ultrapassou o limite do orçamento.')
else:
    print('PARABENS: Voce está dentro do limite do orçamento.')

print(f'Limite estipulado é R$ {limite}')