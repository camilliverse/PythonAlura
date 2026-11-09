projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto is None:
        print('Ausente')
    else:
        print(projeto)