
class CarrinhoDeCompras:
    def __init__(self):
        self._produtos = []

    @property
    def produtos(self):
        return self._produtos

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(f'{produto.quantidade} {produto.nome} - '
                  f'un: R${produto.valor} - Total R${produto.valor * produto.quantidade}')

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor * produto.quantidade
        return f'\nO total deu R${total}'

########################################################################################################################


class Produto:
    def __init__(self, nome, valor, quantidade):
        self._nome = nome
        self._valor = valor
        self._quantidade = quantidade

    @property
    def nome(self):
        return self._nome

    @property
    def valor(self):
        return self._valor

    @property
    def quantidade(self):
        return self._quantidade
