from abc import ABC, abstractmethod


class Conta(ABC):  # Nâo é possível mais instanciá-la directamente, apenas os herdeiros
    def __init__(self, agencia: int, conta: int, saldo: float):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
# ___________________________________________________________________

    @property
    def agencia(self):
        return f'Tua agência é: {self._agencia}'

    @property
    def conta(self):
        return f'Tua conta é: {self._conta}'

    @property
    def saldo(self):
        return f'Teu saldo é: {self._saldo}'
# ___________________________________________________________________

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do depósito precisa ser numérico!')
        self._saldo += valor
        self.detalhes()
# ___________________________________________________________________

    def detalhes(self):
        print(f'Agência: {self._agencia} Conta: {self._conta} Saldo: {self._saldo}\n')
# ___________________________________________________________________

    @abstractmethod  # Obrigando aos herdeiros a terem êsse método embutido
    def sacar(self, valor):  # Não possui nada, pois, será configurado nos herdeiros
        pass

########################################################################################################################


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self._saldo < valor:
            print('Saldo Insuficiente!')
            print(f'\tSaldo disponível para saque: {self._saldo}\n')
            return

        self._saldo -= valor
        self.detalhes()

########################################################################################################################


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super(ContaCorrente, self).__init__(agencia, conta, saldo)
        self._limite = limite
    # ___________________________________________________________________

    @property
    def limite(self):
        return self._limite
    # ___________________________________________________________________

    def sacar(self, valor):
        if (self._saldo + self.limite) < valor:
            print('Saldo Insuficiente')
            print(f'\tSaldo disponível para saque (Saldo + Limite): {self._saldo + self.limite}\n')
            return

        self._saldo -= valor
        self.detalhes()
