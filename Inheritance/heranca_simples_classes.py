
class Pessoa:  # Súper-classe não herda nada das outras classes
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        self.nomeclasse = self.__class__.__name__  # Apenas mostrando o nome da classe quando as herdeiras executam-na

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    def falar(self):
        print(f'{self.nomeclasse} está falando...\n')

########################################################################################################################


class Cliente(Pessoa):  # Herdando os atributos/métodos da classe cliente
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...\n')

########################################################################################################################


class Aluno(Pessoa):  # Herança Multinível — herda de Cliente que herda de Pessoa
    def estudar(self):  # Método estudar só está disponível na classe Aluno
        print(f'{self.nomeclasse} está estudando...\n')
