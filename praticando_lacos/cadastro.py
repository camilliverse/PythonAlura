while True:
    nome = input('Digite seu nome de usuario: ')
    senha = input('Digite sua senha: ')

    if len(nome) < 5:
        print('O nome de usuario deve ter pelo menos 5 carateres')
        continue

    if len(senha) < 8:
        print('A senha deve ter no minimo 8 caracteres')
        continue

    print('Cadastro realizado com sucesso!')
    break