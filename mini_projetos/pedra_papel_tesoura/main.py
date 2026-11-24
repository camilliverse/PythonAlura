import random

#Pedra ganha de Tesoura (Pedra quebra Tesoura);
#Tesoura ganha de Papel (Tesoura corta Papel);
#Papel ganha de Pedra (Papel cobre Pedra);
#Se ambos escolherem a mesma opção, é um empate.

def pedra_papel_tesoura():
    escolhas = ['pedra','papel','tesoura']
    computador = random.choice(escolhas)
    usuario = input('digite sua escolha (pedra,papel,tesoura): ').lower()

    if usuario not in escolhas:
        print('escolha invalida')
        return

    print(f"Computador escolheu: {computador}") 

    if usuario == computador: 
        print("empate") 
    elif ( 
        (usuario == "pedra" and computador == "tesoura") or 
        (usuario == "papel" and computador == "pedra") or 
        (usuario == "tesoura" and computador == "papel") 
    ): 
        print("você venceu!") 
    else: 
        print("você perdeu!") 
    
    pedra_papel_tesoura()
    

