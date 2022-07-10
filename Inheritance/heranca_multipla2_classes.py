
class LogMixinEletronico:  # Log exclusivo do Eletronico
    @staticmethod
    def write(msg):
        with open('log2.log', 'a+') as file:
            file.write(f'{msg}\n')
            file.write('---------------------------------------\n')
    # _____________________________________________________________________

    def log_info(self, msg):
        self.write(f'INFO: {msg}')
    # _________________________________________

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')

########################################################################################################################


class LogMixinSmartphone:  # Log exclusivo do Smartphone
    @staticmethod
    def write(msg):
        with open('log2.log', 'a+') as file:
            file.write(f'{msg}\n')
            file.write('---------------------------------------\n')
    # ________________________________________________________________________________

    # Escrevendo com Tab p'ra identificar o que é Aparelho e o que é Smartphone
    def log_info_phone(self, msg):
        self.write(f'\tINFO: {msg}')
    # ________________________________________________________________________________

    def log_error_phone(self, msg):
        self.write(f'\tERROR: {msg}')

########################################################################################################################


class Eletronico(LogMixinEletronico):  # Herdando de LogMixin p'ra poder mandar o estado actual
    def __init__(self, nome):
        self._nome = nome
        self.__ligado = False
    # _____________________________________________________________________

    @property
    def nome(self):
        return self._nome

    @property
    def ligado(self):
        return self.__ligado

    @ligado.setter  # Modificandoo estado no Aparelho
    def ligado(self, estado=False):
        self.__ligado = estado
    # ______________________________________________________________________________

    def ligar(self):
        if self.ligado:  # Apenas conferindo se já está ligado
            print('O aparelho já está ligado!')
            self.log_error('O usário tentou ligar o aparelho já ligado.')  # Mandando o êrro
            return

        ligou = f'{self.nome} foi ligado!'
        print(ligou)
        self.log_info(ligou)
        self.ligado = True
    # _______________________________________________________________________________

    def desligar(self):
        if not self.ligado:  # Conferindo se está desligado
            print('O aparelho já está desligado!')
            self.log_error('O usuário tentou desligar o aparelho já desligado.')  # Mandando o êrro
            return

        desligou = f'{self.nome} foi desligado!'
        print(desligou)
        self.log_info(desligou)
        self.ligado = False

########################################################################################################################


class Smartphone(Eletronico, LogMixinSmartphone):  # Herdado de Eletronico e LogMixinSmartphone os métodos
    def __init__(self, nome):  # Inicializando o Smartphone usando o __init__ do Aparelho
        super(Smartphone, self).__init__(nome)
        self.__conectado = False
    # _____________________________________________________________________

    @property
    def conectado(self):
        return self.__conectado

    @conectado.setter  # Alterando o estado da conexão
    def conectado(self, estado=False):
        self.__conectado = estado
    # ________________________________________________________________________________________

    def conectar(self):
        if not self.ligado:  # Conferindo se está ligado
            print('O aparelho não está ligado!')
            self.log_error_phone('O usuário tentou conectar o aparelho estando desligado.')
            return

        conectou = f'{self.nome} está conectado!'
        print(conectou)
        self.log_info_phone(conectou)
        self.conectado = True
    # _________________________________________________________________________________________

    def desconectar(self):
        if not self.conectado:  # Conferindo se está conectado
            print('O aparelho já está desconectado!')
            self.log_error_phone(f'O usuário tentou desconectar o {self.nome} já desconectado.')
            return

        desconectou = f'{self.nome} foi desconectado!'
        print(desconectou)
        self.log_info_phone(desconectou)
        self.conectado = False
