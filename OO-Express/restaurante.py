#apara alterar rapidamente use o atalho ctrl +f e seleciona a aba de baixo assim consegue alterar varios metodos com o mesmo nome de uma vez 
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self): #self significa o que está alocado 
        return f'{self.nome} | {self.categoria}' 

    @property
    def ativo(self):
        return '☑' if self._ativo else '☒' 
    
    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(24)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} |{restaurante.categoria.ljust(25)} | {restaurante.ativo}' )


restaurante_mushu = Restaurante('Muschu', "Chinesa")
restaurante_config = Restaurante('Config', "Lanchonete")

Restaurante.listar_restaurantes()