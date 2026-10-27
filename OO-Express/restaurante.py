class restaurante:
    nome = ' '
    categoria = ' '
    ativo = False

restaurante_mushu = restaurante
restaurante_mushu.nome = 'mushu'
restaurante_mushu.categoria = 'chinesa'

restaurante_config = restaurante

restaurantes = [restaurante_mushu , restaurante_config]
print(restaurante_mushu.ativo)