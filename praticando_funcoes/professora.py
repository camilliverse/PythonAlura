def calcular_idade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento

nascimento = int(input('Digite o ano do nascimento: '))
atual = int(input('Digite o ano atual: '))

idade = calcular_idade(nascimento, atual)
print(f'a idade é {idade} anos')

