
class Cliente:
    def __init__(self, nome, idade='Idade não informada'):
        self._nome = nome
        self._idade = idade
        self.__endereco = Endereco()  # Atributo que conecta a classe Endereco

    # Protegendo os atributos
    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @property
    def endereco(self):  # Proteção mais forte p'ra evitar ser sobrescrita
        return self.__endereco

    def __del__(self):
        print(f'\n{self.nome} foi apagado')

########################################################################################################################


class Endereco:
    def __init__(self):  # Não recebe parâmetro, pois, estará conectada a uma classe principal
        self.__enderecos = {}  # O Estado será a chave e as cidades os valores dentro de uma lista

    @property
    def enderecos(self):  # Protegendo o atributo
        return self.__enderecos

    def insere_endereco(self, cidade, estado):
        if estado not in self.enderecos:
            self.enderecos[estado] = [cidade]
        else:
            self.enderecos[estado].append(cidade)

    def lista_enderecos(self):
        for estado, cidades in self.enderecos.items():
            print(f'\t- {estado}')
            for cidade in cidades:
                print(f'\t\t|- {cidade}')

    def __del__(self):
        print(f'{self.enderecos} foi apagado')
