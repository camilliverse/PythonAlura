#utilizamos funções lambda para definir operações básicas e uma estrutura 
#condicional para o menu. O lambda torna o código mais compacto para operações simples.

soma = lambda x, y: x + y 

subtrai = lambda x, y: x - y 

multiplica = lambda x, y: x * y 

divide = lambda x, y: x / y if y != 0 else "Erro: Divisão por zero" 

x = float(input("Digite o primeiro número: ")) 

y = float(input("Digite o segundo número: ")) 

operacao = input("Escolha a operação (| + | - | * | / |): ") 
 
if operacao == '+': 
    print(f"O resultado é: {soma(x, y)}") 
elif operacao == '-': 
    print(f"O resultado é: {subtrai(x, y)}") 
elif operacao == '*': 
    print(f"O resultado é: {multiplica(x, y)}") 
elif operacao == '/': 
    print(f"O resultado é: {divide(x, y)}") 
else: 
    print("Operação inválida")

#Uma abordagem mais eficiente para evitar múltiplas estruturas 
# if-elif é utilizar um dicionário para armazenar as operações matemáticas

operacoes = { 

    '+': soma,  

   '-': subtrai, 

    '*': multiplica, 

    '/': divide 

} 

if operacao in operacoes:  

   resultado = operacoes[operacao](x, y)  

   print(f"O resultado é: {resultado}")  

else:  

   print("Operação inválida")


