from classes_molde import Pessoa

pessoa1 = Pessoa('Raphaël', 23)

pessoa1.comer('pão')
pessoa1.parar_comer()
pessoa1.falar('trabalhar com programação')
pessoa1.parar_falar()
pessoa1.falar_com_pessoa('trampar de casa', 'Matthäus')
print(pessoa1.idade)
print(pessoa1.get_ano_nascimento())


# Usando classmethod
pessoa2 = Pessoa.por_ano_nascimento('Marcos', 1990)
print(f'{pessoa2.nome} tem {pessoa2.idade} anos de idade.')

# Usando staticmethod
print(f'O ID do {pessoa2.nome} é {Pessoa.gera_id()}')
