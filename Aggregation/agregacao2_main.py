from agregacao2_classes import Produto, Carrinho


carrinho = Carrinho()
p1 = Produto('Camisa', 10, 2)
p2 = Produto('Calça', 20, 1)
p3 = Produto('Cueca', 15, 2)

carrinho.adicionar_produto(p1)
carrinho.adicionar_produto(p1)
carrinho.adicionar_produto(p2)
carrinho.adicionar_produto(p3)

carrinho.listar_produtos()

print(carrinho.soma_total())

print()
print(carrinho.produtos)
