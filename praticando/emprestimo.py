emprestimo = float(input('Digite o valor do emprestimo (R$): '))
parcela = float(input('Digite o valor da parcela (R$): '))

if emprestimo > 2000 and parcela < 0.3 * emprestimo: #basicamente é se meu emprestimo for maior que 2000 e minha parcela for menor que 30% multiplique pelo meu emprestimo
    print('Aprovado!')
elif emprestimo <= 2000:
    print('Negado! Renda insuficiente')
else:
    print('Negado! Parcela acima de 30%')