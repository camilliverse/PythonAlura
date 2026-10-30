class ContaBancaria:

    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self.ativo = False

    def __str__(self):
        return f'Titular: {self._titular} | Saldo: R${self._saldo:.2f}'

    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo


# Exercício 2
conta1 = ContaBancaria('Alice', 1500)
conta2 = ContaBancaria('Luiza', 2500)

print(conta1)
print(conta2)

# Exercício 3
ContaBancaria.ativar_conta(conta1)
print(conta1.ativo)

# Exercício 5
print(conta1.titular)