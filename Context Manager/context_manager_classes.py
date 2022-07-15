from contextlib import contextmanager


class Arquivo:
    def __init__(self, arquivo, modo):
        print('Abrindo o arquivo!')
        self.arquivo = open(arquivo, modo)  # Apenas abriu o arquivo
    # ______________________________________________________

    def __enter__(self):  # Método chamado quando entra na classe
        print('Retornando o arquivo!')
        return self.arquivo  # Retornando o arquivo p'ra variável criada
    # ______________________________________________________

    def __exit__(self, exc_type, exc_val, exc_tb):  # Método de saída, quando o 'with' termiina de ser executado
        print('Fechando o arquivo!')
        self.arquivo.close()
        print(exc_type)  # Caso tenha algum êrro, serão executados
        print(exc_val)  # Caso contrário aparecerá 'None'
        print(exc_tb)  # Posso tratar caso tenha algum tipo desses êrros
        return True  # Faz o êrro não aparecer na tela (bom usar isso após tratá-lo)

########################################################################################################################


class File:  # Modo mais fácil de criar-se um gerenciador de contexto
    @contextmanager  # Função decoradora
    def abrir(self, arquivo, modo):
        try:
            print('Abrindo o arquivo!')
            arquivo = open(arquivo, modo)
            yield arquivo  # Retornando o arquivo (não se usa 'return' para a função não parar de funcionar)
        finally:
            print('Fechando o arquivo!')
            arquivo.close()

########################################################################################################################


@contextmanager
def abrir(arquivo, modo):  # Mesma coisa do class File, contudo, n'uma função e não n'um método na classe
    try:
        print('Abrindo o arquivo!')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('Fechando o arquivo!')
        arquivo.close()
