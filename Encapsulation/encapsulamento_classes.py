
class BaseDeDadosPublica:
    def __init__(self):
        self.dados = {}  # A parte mais importante da classe está desprotegida

    def inserir_cliente(self, id, nome):
        if 'Clientes' not in self.dados:
            self.dados['Clientes'] = {id: nome}
        else:
            self.dados['Clientes'].update({id: nome})

    def listar_clientes(self):
        for id, nome in self.dados['Clientes'].items():
            print(f'\tNome: {nome} - Identificação: {id}')

    def apaga_cliente(self, id):
        del self.dados['Clientes'][id]

########################################################################################################################


class BaseDeDadosPrivadaFraca:
    def __init__(self):
        self._dados = {}  # A parte mais importante da classe tem uma proteção fraca

    @property  # Utilizei um getter p'ra conseguir vizualizar os valores de fora da classe
    def dados(self):
        return self._dados

    def inserir_cliente(self, id, nome):
        if 'Clientes' not in self._dados:
            self._dados['Clientes'] = {id: nome}
        else:
            self._dados['Clientes'].update({id: nome})

    def listar_clientes(self):
        for id, nome in self._dados['Clientes'].items():
            print(f'\tNome: {nome} - Identificação: {id}')

    def apaga_cliente(self, id):
        del self._dados['Clientes'][id]

########################################################################################################################


class BaseDeDadosPrivadaForte:
    def __init__(self):
        self.__dados = {}  # A parte mais importante da classe tem uma proteção forte

    @property  # Utilizei um getter p'ra conseguir vizualizar os valores de fora da classe
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'Clientes' not in self.__dados:
            self.__dados['Clientes'] = {id: nome}
        else:
            self.__dados['Clientes'].update({id: nome})

    def listar_clientes(self):
        for id, nome in self.__dados['Clientes'].items():
            print(f'\tNome: {nome} - Identificação: {id}')

    def apaga_cliente(self, id):
        del self.__dados['Clientes'][id]
