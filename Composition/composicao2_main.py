from composicao2_classes import Cliente

cliente1 = Cliente('Marcelo')
cliente1.endereco.insere_endereco('Værøy', 'Nordland')
cliente1.endereco.insere_endereco('Bodø', 'Nordland')

print(cliente1.nome)
cliente1.endereco.lista_enderecos()
del cliente1
print('---------------------')

########################################################################################################################

cliente2 = Cliente('Irene')
cliente2.endereco.insere_endereco('Øvre Eiker', 'Viken')
cliente2.endereco.insere_endereco('Skjåk', 'Innlandet')
cliente2.endereco.insere_endereco('Tysvær', 'Rogaland')

print(cliente2.nome)
cliente2.endereco.lista_enderecos()
print('---------------------')

########################################################################################################################

cliente3 = Cliente('Pedro')
cliente3.endereco.insere_endereco('Iveland', 'Agder')

print(cliente3.nome)
cliente3.endereco.lista_enderecos()

########################################################################################################################

# Representação visual de quando o arquivo começar a apagar os dados não úteis
print('\n##########################################################')
