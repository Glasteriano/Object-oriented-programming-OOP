
class EksistererIkkjeError(Exception): pass
# Apenas isso é necessário para criar-se uma exceção
# Tem que herdar de Exception p'ra funcionar

########################################################################################################################


class ConteudoDentro:
    @staticmethod
    def testar(*args, **kwargs):  # Caso não receba parâmetro, mostrará o êrro
        error = EksistererIkkjeError('Êrro criado e não pré-programado.')

        if len(args) != 0 or len(kwargs) != 0:
            print(f'{args}\n{kwargs}')
        else:
            print(error)

########################################################################################################################


class Vazio:
    @staticmethod
    def nada():  # Levanta um êrro para ser testado
        raise EksistererIkkjeError('Êrro levantado com sucesso!')  # Mensgagem a ser mostrada

    def executando_nada(self):  # Tentará executar nada(), mas como não recebe parâmetro dará êrro
        try:
            return self.nada()
        except EksistererIkkjeError as error:
            print(f'Êrro: {error}')  # Mostrando o êrro
