
class Carrinho:
    def __init__(self):
        self.__produtos = {}

    @property  # Dando acesso ao atributo protegido
    def produtos(self):
        return self.__produtos

    def adicionar_produto(self, produto):
        # Vejo se o produto já não existe no carrinho e adiciono-o
        if produto.nome not in self.produtos.keys():
            self.produtos[produto.nome] = {'Quantidade': produto.quantidade,
                                           'Valor Unitário': produto.valor,
                                           'Valor Total': produto.quantidade * produto.valor}
        else:
            # Caso exista, apenas modifico os valores de Quantidade e Valor Total
            self.produtos[produto.nome]['Quantidade'] += produto.quantidade
            self.produtos[produto.nome]['Valor Total'] += produto.quantidade * produto.valor
            # Adiciono a multiplicação da nova quantidade com o valor à quantidade já existente lá

    def listar_produtos(self):
        # Listo os valores mudando o ponto (.) pela vírgula (,) para melhor visualização
        for produto, valores in self.produtos.items():
            valor_total = f'{valores["Valor Total"]:.2f}'
            valor_unitario = f'{valores["Valor Unitário"]:.2f}'
            print(f'Produto: {produto}\n\tQuantidade: {valores["Quantidade"]}\n'
                  f'\tValor Unitário: R${str(valor_unitario).replace(".", ",")}\n'
                  f'\tValor Total: R${str(valor_total).replace(".", ",")}\n')

    def soma_total(self):
        total = 0
        for _, valor in self.produtos.items():
            total += valor['Valor Total']
        total = f'{total:.2f}'
        return f'O valor total da compra deu R${str(total).replace(".", ",")}'

########################################################################################################################


class Produto:
    def __init__(self, nome, valor, quantidade):
        self._nome = nome
        self._valor = float(valor)
        self._quantidade = int(quantidade)

    @property
    def nome(self):
        return self._nome

    @property
    def valor(self):
        return self._valor

    @property
    def quantidade(self):
        return self._quantidade
