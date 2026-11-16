
participantes = { 

    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

}

print(f'{participantes}')

nome_remover = input("Digite  o  nome do participante a ser removido: ")

for worksho, nomes in participantes.items():
    nomes.discard(nome_remover)

print("Lista atualizada de participantes:")

for workshop, nomes in participantes.items():
    print(f'{worksho}: {nomes}')