class Pessoa:

    def __init__(self, nome=' ', idade=0, profissao=' '):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá {self.nome}! trabalha com {self.profissao}'
        else:
            return f'Olá {self.nome}!'

    def aniversario(self):
        self.idade += 1


alice = Pessoa(nome='Alice', idade=25, profissao='Engenheira')

print(alice)
print(alice.saudacao)

alice.aniversario()
print(alice.idade)