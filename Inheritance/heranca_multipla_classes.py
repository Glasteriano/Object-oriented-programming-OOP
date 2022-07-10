
class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self.ligado = False

    @property
    def nome(self):
        return self._nome

    def ligar(self):
        if self.ligado:
            return

        print(f'{self._nome} foi ligado!')
        self.ligado = True

    def desligar(self):
        if not self.ligado:
            return

        print(f'{self._nome} foi desligado!')
        self.ligado = False

########################################################################################################################


class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')

########################################################################################################################


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self.conectado = False

    def conectar(self):
        if not self.ligado:
            info = f'{self._nome} não está ligado!'
            print(info)
            self.log_error(info)
            return

        if self.conectado:
            error = f'{self._nome} já está conectado!'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} está conectado!'
        print(info)
        self.log_info(info)
        self.conectado = True

    def desconectar(self):
        if not self.conectado:
            error = f'{self._nome} não está conectado!'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} foi desconectado com sucesso!'
        print(info)
        self.log_info(info)
        self.conectado = False
