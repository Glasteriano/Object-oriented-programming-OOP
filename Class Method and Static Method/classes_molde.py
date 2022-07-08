from datetime import datetime
from random import randint


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    @classmethod  # Relacionado apenas à Classe e não às pessoas criadas a partir dessa classe
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod  # Função comum que não usa nada presente na Classe
    def gera_id():  # Por isso não tem parâmetros, a não ser que na própria função hão de ser usados
        id_aleatorio = randint(1000, 9999)
        # return id_aleatorio
        return f'{str(id_aleatorio)[:2]}-{str(id_aleatorio)[2:]}'
        # Pego o número gerado e parto-o em dois com um traço '-'
        # 12-34 é o mesmo que 1234

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar_com_pessoa(self, assunto, nome_outra_pessoa):
        if self.comendo:
            print(f'{self.nome} não pode falar com outros comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto} com {nome_outra_pessoa}.')
        self.falando = True

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f"{self.nome} não pode comer falando.")
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
