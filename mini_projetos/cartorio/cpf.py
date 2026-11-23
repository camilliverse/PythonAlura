import re

def validar_cpf(cpf):
    if not cpf.isdigit():
        return 'ERRO: O CPF deve conter apenas numeros'
    if len(cpf) != 11:
        return "Erro: O CPF deve ter exatamente 11 digitos"
    return 'CPF valido'

cpf = input('digite seu cpf: ')
print(validar_cpf(cpf))
