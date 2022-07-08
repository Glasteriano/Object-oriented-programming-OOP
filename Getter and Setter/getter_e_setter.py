class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):  # Correção do preço caso seja uma string
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor


produto_1 = Produto('Calça', 80)
print(produto_1.preco)
produto_1.desconto(20)
print(produto_1.preco)

produto_2 = Produto('Casaco', 'R$150')  # Preço enviado em forma de string e não inteiro/float
p2 = produto_2.preco
print(p2)
