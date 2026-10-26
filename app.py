import os

restaurantes = [
{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False}, {'nome': 'Pizza Suprema', 'categoria': 'Italizana', 'ativo': True}, 
{'nome': 'Cantina', 'categoria': 'Arabe', 'ativo': False}]

def exibir_nome_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_programa():
    exibir_subtitulos('-- Finalizando o app --\n')
    
def voltar_ao_menu_principal(): 
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def exibir_subtitulos(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(texto)

def opcao_invalida():
    print('Opção inválida')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulos('--- Cadastro de novos restaurantes ---\n')
  
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante{nome_restaurante}: ')
    dados_do_restaurnate = {'nome': nome_restaurante , 'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_do_restaurnate)
    restaurantes.append(nome_restaurante)

    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()

def Listar_restaurantes(): 
    exibir_subtitulos('--- Listar restaurantes ---\n')
    print()

    for restaurante in restaurantes: 
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    exibir_subtitulos('Alterando estado restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurantes['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante{nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Voce escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            Listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

