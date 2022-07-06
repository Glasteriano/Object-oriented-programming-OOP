
class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

########################################################################################################################


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    @staticmethod
    def escrever():
        print('A caneta está escrevendo...')

    def escrevendo(self, nome):
        print(f'{nome} está escrevendo com a caneta {self.__marca}.')

########################################################################################################################


class MaquinaDeEscrever:
    @staticmethod
    def escrever():
        print('A máquina está escrevendo...')

    @staticmethod
    def escrevendo(nome):
        print(f'{nome} está escrevendo com a máquina.')
