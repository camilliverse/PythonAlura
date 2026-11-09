nota1 = int(input('Digite a primeira nota do aluno: '))
nota2 = int(input('Digite a segunda nota do aluno: '))
nota3 = int(input('Digite a terceira nota do aluno: '))

media = (nota1 + nota1 + nota3) / 2


print(f'Media total é: {media}')

if media >= 7:
    print('Aluno aprovado')
elif 5 <= media < 7:
    print('Recuperação')
else:
    print('Aluno reporvado')

