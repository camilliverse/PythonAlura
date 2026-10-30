from restaurante import Restaurante

restaurante_mushu = Restaurante('Muschu', "Chinesa")
restaurante_arriba = Restaurante('Arriba mexico', 'Mexicana')
restaurante_arigato = Restaurante('Arigato japa', 'Japones')

restaurante_arriba.alternar_status()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()