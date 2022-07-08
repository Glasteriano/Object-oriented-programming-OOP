
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        self.nomeclasse = self.__class__.__name__

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    def falar(self):
        print(f'{self.nomeclasse} está falando...')

########################################################################################################################


class CLiente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')

    def falar(self):  # Mesmo nome em Pessoa, fazendo com que falar() em Pessoa não possa mais ser usado em Cliente
        print('Estou em CLIENTE!')

########################################################################################################################

# Super() possibilita de uma função executar funções de quem herdou sem precisar reescrever na nova classe (para não
# ficar repetitivo) e também chamar funções herdades primeiro caso na classe herdeira tenha o mesmo nome da função
# herdade. Caso não chame super() essa função de nome igual deixará de ser executada da classe herdada (superclasse)
# e passará apenas a ser executada na função herdeira (fazendo com que esse método não possa ser chamada da classe-mãe


class ClienteVIP(CLiente):  # Herda de Cliente que acaba herdando de Pessoa por tabela
    def __init__(self, nome, sobrenome, idade):  # Mesmo nome que de função de quem herdeou
        super().__init__(nome, idade)  # Super() executa __init__ de quem herdou primeiro (no caso de Pessoa)
        self.sobrenome = sobrenome

    def falar(self):  # Mesmo nome de função de Pessoa e Cliente
        Pessoa.falar(self)  # Especificando de qual classe quero usar a função falar() primeiro
        CLiente.falar(self)  # Caso contrário pararia na primeira vez que encontrar o método igual
        print(f'{self.nome} {self.sobrenome}')  # Para depois executar o comando em ClienteVIP
