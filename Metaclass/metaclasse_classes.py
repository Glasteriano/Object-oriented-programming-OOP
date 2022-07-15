class MetaZero(type):
    def __new__(mcs, name, bases, namespace):
        print(f'● Classe [{name}] da metaclasse "{__class__.__name__}"')  # Mostra quais classes herdam da Metaclasse
        print(f'\t- A classe [{name}] herda de {bases}\n')

        return type.__new__(mcs, name, bases, namespace)

########################################################################################################################


class One(metaclass=MetaZero):
    def fala(self):
        self.b_fala()  # Chama uma função na classe-filha B (não é muito comum fazer isso)

########################################################################################################################


class Two(One):
    pass  # Como B não possui o método b_fala, assim que instanciar o método fala o código dará êrro

########################################################################################################################
########################################################################################################################
########################################################################################################################


class MetaOne(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'Three':  # Ignorando a classe-pai chamada 'three'
            return type.__new__(mcs, name, bases, namespace)

        print(f'● Classe [{name}] da metaclasse \'{__class__.__name__}\'')
        print(f'\t- A classe [{name}] herda de {bases}')
        print(f'\n\t- Os atributos/métodos dentro das classe-filha [{name}] são:')

        for key, value in namespace.items():  # Printando os atributos/métodos nas classes herdeiras
            print(f'\t\t->  {key}: {value}')  # Como namespace é um dict, posso iterar
        print()  # Só p'ra pular linha

        return type.__new__(mcs, name, bases, namespace)

########################################################################################################################


class Three(metaclass=MetaOne):
    pass  # Não criando nada, pois, será ignorado no MetaOne

########################################################################################################################


class Four(Three):
    teste = 'Só uma string'

    @staticmethod
    def dunno():
        pass

########################################################################################################################


class Five(Three):
    teste_2 = 'Outra string'

    def __init__(self, nome):  # Apenas p'ra diferenciar do staticmethod
        print(f'Oi, {nome}')

########################################################################################################################
########################################################################################################################
########################################################################################################################


class MetaTwo(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'Six':  # Ignorando a classe-pai
            return type.__new__(mcs, name, bases, namespace)

        print(f'● Classe [{name}] da metaclasse \'{__class__.__name__}\'')

        if 'b_fala' not in namespace:  # Conferindo se tem o método na Classe
            print(f'\t ●● Esta classe precisa ter o método \'b_fala\'\n')

        print(f'\t- A classe [{name}] herda de {bases}')
        print(f'\n\t- Os atributos/métodos dentro das classe-filha [{name}] são:')

        for key, value in namespace.items():  # Printando os atributos/métodos detro das classes herdeiras
            print(f'\t\t->  {key}: {value}')  # Como namespace é um dict, posso iterar
        print()  # Só p'ra pular linha

        return type.__new__(mcs, name, bases, namespace)

########################################################################################################################


class Six(metaclass=MetaTwo):
    pass

########################################################################################################################


class Seven(Six):
    pass

########################################################################################################################


class Eight(Six):
    b_fala = 'Retirando a mensagem de êrro'

########################################################################################################################
########################################################################################################################
########################################################################################################################


class MetaThree(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'Nine':
            return type.__new__(mcs, name, bases, namespace)

        print(f'● Classe [{name}] da metaclasse \'{__class__.__name__}\'')

        if 'b_fala' not in namespace:
            print(f'\t ●● Esta classe precisa ter o método \'b_fala\'\n')
        else:
            if not callable(namespace['b_fala']):  # Conferindo se é realmente um método (função) staticmethod não funfa
                print(f'\t ●● \'b_fala\' tem que ser um MÉTODO e não um atributo!\n')

        print(f'\t- A classe [{name}] herda de {bases}')
        print(f'\n\t- Os atributos/métodos dentro das classe-filha [{name}] são:')

        for key, value in namespace.items():
            print(f'\t\t->  {key}: {value}')
        print()  # Só p'ra pular linha

        return type.__new__(mcs, name, bases, namespace)

########################################################################################################################


class Nine(metaclass=MetaThree):
    pass

########################################################################################################################


class Ten(Nine):
    b_fala = 'Evitando o primeiro êrro'

########################################################################################################################


class Eleven(Nine):
    def b_fala(self):  # Se mudar para estático, entra no êrro do método
        print('Evitando o segundo êrro')

########################################################################################################################


class Twelve(Nine):
    pass

########################################################################################################################
########################################################################################################################
########################################################################################################################


class MetaFour(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'Thirteen':
            return type.__new__(mcs, name, bases, namespace)

        if 'atributo1' in namespace:  # Evitando que o atributo seja sobrescrito, deletando os outros
            del namespace['atributo1']

        print(f'● Classe [{name}] da metaclasse \'{__class__.__name__}\'')
        print(f'\t- A classe [{name}] herda de {bases}')
        print(f'\n\t- Os atributos/métodos dentro das classe-filha [{name}] são:')

        for key, value in namespace.items():
            print(f'\t\t->  {key}: {value}')
        print()  # Só p'ra pular linha

        return type.__new__(mcs, name, bases, namespace)

########################################################################################################################


class Thirteen(metaclass=MetaFour):
    atributo1 = 'Valor da Classe Thirteen'

########################################################################################################################


class Fourteen(Thirteen):
    atributo1 = 'Valor da Classe Fourteen'  # não vai aparecer no namespace da Metaclasse
    atributo2 = 'Outro valor da Classe Fourteen'

########################################################################################################################
########################################################################################################################
########################################################################################################################


class MetaFive(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'Fifteen':
            return type.__new__(mcs, name, bases, namespace)

        if 'atributo1' in namespace:  # Evitando que o atributo seja sobrescrito, deletando os outros
            print(f'\t\t●●● A Classe {name} tentou sobrescrever o atributo em {bases}!\n')
            del namespace['atributo1']

        print(f'● Classe [{name}] da metaclasse \'{__class__.__name__}\'')
        print(f'\t- A classe [{name}] herda de {bases}')
        print(f'\n\t- Os atributos/métodos dentro das classe-filha [{name}] são:')

        for key, value in namespace.items():
            print(f'\t\t->  {key}: {value}')
        print()  # Só p'ra pular linha

        return type.__new__(mcs, name, bases, namespace)

########################################################################################################################


class Fifteen(metaclass=MetaFive):
    atributo1 = 'Valor da Classe Fifteen'

########################################################################################################################


class Sixteen(Fifteen):
    atributo1 = 'Valor da Classe Sixteen'  # não vai aparecer no namespace da Metaclasse
    atributo2 = 'Outro valor da Classe Sixteen'

########################################################################################################################


class Seventeen(Fifteen):
    atributo1 = 'Valor da Classe Seventeen'  # não vai aparecer no namespace da Metaclasse
    atributo2 = 'Outro valor da Classe Seventeen'

########################################################################################################################
########################################################################################################################
########################################################################################################################


A = type('Eighteen', (), {'atributo2': 'Hei Verden!'})

a = A()
print(a.atributo2)

########################################################################################################################
########################################################################################################################
########################################################################################################################


class Father:
    atributo3 = 'Só um teste'


B = type('Nineteen', (Father,), {'atributo4': 'Hei Verden!'})

b = B()
print(b.atributo3)
