from agregacao_classes import Produto, CarrinhoDeCompras

carrinho = CarrinhoDeCompras()
p1 = Produto('Camisa', 45, 2)
p2 = Produto('Caneca', 25, 1)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)


carrinho.listar_produtos()
print(carrinho.soma_total())


