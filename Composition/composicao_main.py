from composicao_classes import Cliente

cliente1 = Cliente('Thor', 30)
cliente1.insere_endereco('Trondheim', 'Trøndelag')
print(cliente1.nome)
cliente1.lista_enderecos()
print()

######################################################################

cliente2 = Cliente('Marja', 40)
cliente2.insere_endereco('Gamle Oslo', 'Oslo')
cliente2.insere_endereco('Bergen', 'Vastland')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

######################################################################

cliente3 = Cliente('Pedro', 25)
cliente3.insere_endereco('Bærum', 'Viken')
print(cliente3.nome)
cliente3.lista_enderecos()
print('\n################################################################')

