class Musica:

    muscias = []

    def __init__(self):
        self.nome = ''
        self.artista = ''
        self.duracao = int
        Musica.muscias.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista}'

    def listar_artistas():
        for muscias in Musica.muscias:
            print({f'{muscias.nome} | {muscias.artista}'})

muscias_billie = Musica ('LUNCH', 'Billie ellish')
muscias_malcolm_tood = Musica ('Malcolm Tood' , 'Earrings')

Musica.listar_artistas()
