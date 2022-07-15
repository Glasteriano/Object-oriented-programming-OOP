# https://rszalski.github.io/magicmethods/
# Material de consulta

class A:
    def __init__(self):
        print('Eu sou o INIT da Classe A\n')  # Será printado isso assim que a classe for instanciada

########################################################################################################################


class B:
    def __new__(cls, *args, **kwargs):  # Primeira coisa a ser chamada (quem constrói a classe com o INIT)
        pass
    # ________________________________________________________

    def __init__(self):
        print('Eu sou o INIT da Classe B\n')  # Não será executado, já que o new não tem nada

########################################################################################################################


class C:
    def __new__(cls, *args, **kwargs):  # Primeira coisa a ser chamada (quem constrói a classe com o INIT)
        print('Eu sou o NEW da Classe C')  # Será executado primeiro isso

        return super().__new__(cls)  # Fazendo o INIT voltar a funcionar
        # Em Python toda Classe deriva de object, por usso o super() funciona
        # Mesmo que object.__new__(cls)
    # ________________________________________________________

    def __init__(self):
        print('Eu sou o INIT da Classe C\n')

########################################################################################################################


class D:
    def __new__(cls, *args, **kwargs):

        cls.nome = 'Tor Odinson'  # Defini um atributo de classe

        return super().__new__(cls)  # Fazendo o INIT voltar a funcionar
    # ________________________________________________________

    def __init__(self):
        print('Eu sou o INIT da Classe D')

########################################################################################################################


class E:
    def __new__(cls, *args, **kwargs):

        def fala_oi(*args, **kwargs):  # Definindo uma função
            print('Olá, tudo bem?\n')

        cls.fala_oi = fala_oi  # Método criado

        return object.__new__(cls)
    # ________________________________________________________

    def __init__(self):
        print('Eu sou o INIT da Classe E')

########################################################################################################################


class F:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_jaexiste'):  # Fazendo todas as instâncias de F serem uma cópia da 1.ª
            cls._jaexiste = object.__new__(cls)  # Criando essa Classe caso não exista

        return cls._jaexiste
    # ________________________________________________________

    def __init__(self):
        print('Eu sou o INIT da Classe F')  # Não será executado, já que o

########################################################################################################################


class G:
    def __init__(self):
        print('Eu sou o INIT da Classe G')
    # ________________________________________________________

    def __call__(self, *args, **kwargs):  # Faz a intância da Classe se comportar como função
        print(args)  # Posso fazer qualquer coisa aqui
        print(kwargs)  # Estou apenas mostrando os argumentos recebidos

########################################################################################################################


class H:
    def __init__(self):
        print('Eu sou o INIT da Classe H')
    # ________________________________________________________

    def __call__(self, *args: float, **kwargs):  # Faz a intância da Classe se comportar como função
        resultado = 1

        for numero in args:  # Multiplicando os numeros recebidos entre si
            resultado *= numero

        return resultado
    # ________________________________________________________

    @staticmethod
    def hello():  # A classe funciona normalmente com as suas funções
        print('Hi from class H\n')

########################################################################################################################


class I:
    def __init__(self):
        print('Eu sou o INIT da Classe I')
    # ________________________________________________________

    def __setattr__(self, key, value):  # É chamado toda a vez que configuro um atrubuto novo
        print(f'Chave/atributo: {key}\nValor: {value}\n')

########################################################################################################################


class J:
    def __init__(self):
        print('Eu sou o INIT da Classe J')
    # ________________________________________________________

    def __setattr__(self, key, value):  # É chamado toda a vez que configuro um atributo novo
        self.__dict__[key] = value  # Settando o atributo ao seu valor

########################################################################################################################


class L:
    def __init__(self):
        print('Eu sou o INIT da Classe L')
    # ________________________________________________________

    def __setattr__(self, key, value):  # É chamado toda a vez que configuro um atributo novo
        if key == 'nome':  # Alterando o valor do atributo caso seja nome
            self.__dict__[key] = 'Vossa mercê não pode fazer isto'
        else:
            self.__dict__[key] = value  # Voltando o comportamento padrão

########################################################################################################################


class M:
    def __init__(self):
        print('Eu sou o INIT da Classe M')
    # ________________________________________________________

    def __str__(self):  # Toda a vez que tentar usar a Classe como ‘string’, êste método será executado
        return 'Esta é a Classe M criada como exemplo'
        # Posso mandar alguma informação útil quando tentarem printar a classe

########################################################################################################################


class N:
    def __init__(self):
        print('Eu sou o INIT da Classe N')
    # ________________________________________________________

    def __len__(self):  # Método que é chamado quando uso o len()
        return 55  # Posso modificar para, por exemplo, contar algo em Base de Dados e retornar-me o valor
