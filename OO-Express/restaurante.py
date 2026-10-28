class restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_mushu = restaurante('Muschu', "Chinesa")
restaurante_config = restaurante('Config', "Lanchonete")

restaurantes = [restaurante_mushu , restaurante_config]
print(restaurante_mushu.ativo)

print(vars(restaurante_mushu))
print(vars(restaurante_config))