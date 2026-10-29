#apara alterar rapidamente use o atalho ctrl +f e seleciona a aba de baixo assim consegue alterar varios metodos com o mesmo nome de uma vez 
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self): #self significa o que está alocado 
        return f'{self.nome} | {self.categoria}' 
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} |{restaurante.categoria} | {restaurante.ativo}' )

restaurante_mushu = Restaurante('Muschu', "Chinesa")
restaurante_config = Restaurante('Config', "Lanchonete")

Restaurante.listar_restaurantes()