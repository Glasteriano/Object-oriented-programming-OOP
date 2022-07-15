from abc import ABC, abstractmethod
# Python não suporta o polimosfismo de sobrecarga, apenas o de sobreposição


class A(ABC):  # Incorporando o método abstrato
    @abstractmethod  # Obrigando os herdeiros a terem o método falar
    def falar(self, mensagem): pass  # Todos os hedeiros devem ter os mesmos parâmetros (self, mensagem)

########################################################################################################################


class B(A):
    def falar(self, mensagem):  # Sobrescrevendo o método falar p'ra agir de modo diferente
        print(f'B snakker om {mensagem}!')

########################################################################################################################


class C(A):
    def falar(self, mensagem):  # Outra ação diferene de A e B
        print(f'C snakker om {mensagem}!')
