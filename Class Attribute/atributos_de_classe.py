# Exemplo 1

class A:
    vc = 'Valor original de dentro da classe A!'
    # Como não tenho nenhum inicializador para haver possíveis divergências


a1 = A()
a2 = A()

print(f'a1 = {a1.vc}')  # Acesso tanto pelas instâncias atribuídas
print(f'a2 = {a2.vc}')
print(f'class A = {A.vc}')  # Como directamente pela classe

########################################################################################################################

# Exemplo 2


class B:
    vc = 'Valor original de dentro da classe B!'


b1 = B()
b2 = B()

B.vc = 'Valor da classe B modificado de fora dela!'
# A variável da classe foi modificada por inteira, então todas as instâncias serão afectadas

print(f'b1 = {b1.vc}')
print(f'b2 = {b2.vc}')
print(f'class B = {B.vc}')

########################################################################################################################

# Exemplo 3


class C:
    vc = 'Valor original de dentro da classe C!'


c1 = C()
c2 = C()

c1.vc = 'Valor da instância alterado!'

print(f'c1 = {c1.vc}')  # Modifiquei o valor apenas do c1, por isso não afectou o resto
print(f'c2 = {c2.vc}')
print(f'class C = {C.vc}')

########################################################################################################################

# Exemplo 4


class D:
    vc = 'Valor original de dentro da classe D!'

    def __init__(self):
        self.vc = 'Valor original de dentro da FUNÇÃO INICIALIZADORA!'
        # Como há um construtor agora, qualquer instância será associada agora a ela
        # Mesmo que tenha nome comflictante


d1 = D()
d2 = D()

print(f'd1 = {d1.vc}')
print(f'd2 = {d2.vc}')
print(f'class D = {D.vc}')  # Agora só será possível acessar o valor referindo-se a classe inteira
