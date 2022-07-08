from heranca_simples_classes import Pessoa, Cliente, Aluno

cliente1 = Cliente('Igor', 32)
print(cliente1.nome)
cliente1.comprar()
cliente1.falar()  # Acessando um módulo que existe na classe Pessoa

########################################################################################################################

aluno1 = Aluno('Carlos', 19)
print(aluno1.nome)
aluno1.estudar()

########################################################################################################################

pessoa1 = Pessoa('Roberto', 40)
print(pessoa1.nome)
pessoa1.falar()
