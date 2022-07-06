from encapsulamento_classes import BaseDeDadosPublica
from encapsulamento_classes import BaseDeDadosPrivadaFraca
from encapsulamento_classes import BaseDeDadosPrivadaForte

# Usando uma classe de acesso público

base_publica = BaseDeDadosPublica()

base_publica.inserir_cliente(1, 'Rafael')
base_publica.inserir_cliente(2, 'Matheus')
base_publica.inserir_cliente(3, 'Gabriel')
print(f'\nLista de Clientes - Público\n\t{base_publica.dados}\n')
base_publica.listar_clientes()


base_publica.dados = 'Base Pública deixou de ser um dicionário!!!'
print(f'\n\t\t{base_publica.dados}')
# Dados modificado de dentro da classe fàcilmente

# Descomentar p'ra ver o êrro
"""
base_publica.inserir_cliente(4, 'Marcos')
base_publica.lista_clientes()  # O código dá êrro quando tenta inserir e nem mostra da modificação p'ra baixo
"""
########################################################################################################################

# Usando uma classe com proteção fraca

base_fraca = BaseDeDadosPrivadaFraca()

base_fraca.inserir_cliente(1, 'Håkan')
base_fraca.inserir_cliente(2, 'Bjørn')
base_fraca.inserir_cliente(3, 'Lars')
print(f'\nLista de Clientes - Privado Fraco\n\t{base_fraca.dados}\n')
base_fraca.listar_clientes()

base_fraca._dados = 'Base Fraca deixou de ser um dicionário!!!'
# Mesmo tendo protecção, ainda não é tão difícil alterar

print(f'\n\t\t{base_fraca._dados}')
# O próprio PyCharm acusa de tentar acessar algo protegido

# Descomentar p'ra ver o êrro
"""
base_fraca.inserir_cliente(4, 'Oli')
base_fraca.listar_clientes()
"""
########################################################################################################################

# Usando uma classe com protecção forte

base_forte = BaseDeDadosPrivadaForte()

base_forte.inserir_cliente(1, 'Tor')
base_forte.inserir_cliente(2, 'Odin')
base_forte.inserir_cliente(3, 'Loke')
print(f'\nLista de Clientes - Privado Forte\n\t{base_forte.dados}\n')
base_forte.listar_clientes()

base_forte._BaseDeDadosPrivadaForte__dados = 'Base Forte deixou de ser um dicionário!'
# Nota-se que é muito mais difícil alterar o valor agora
# Não há como alguém sobrescrever sem querer

print(f'\n\t\t{base_forte._BaseDeDadosPrivadaForte__dados}')
# O próprio PyCharm acusa de tentar acessar algo protegido

# Descomentar p'ra ver o êrro
"""
base_forte.inserir_cliente(4, 'Frøya')
base_forte.listar_clientes()
"""