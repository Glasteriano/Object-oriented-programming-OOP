"""
Operador    Método          Operação
------------------------------------------------------
+           __add__         adição
-           __sub__         subtração
*           __mul__         multiplicação
/           __div__         divisão
//          __floordiv__    divisão inteira
%           __mod__         Módulo
**          __pow__         Potência
+           __pos__         Positivo
-           __neg__         Negativo
<           __lt__          Menor que
>           __gt__          Maior que
<=          __le__          Menor ou igual a
>=          __ge__          Maior ou igual a
==          __eq__          Igual a
!=          __ne__          Diferente de
<<          __lshift__      Deslocamento para a esquerda
>>          __rshift__      Deslocamento para a direita
&           __and__         E bit-a-bit
|           __or__          OU bit-a-bit
^           __xor__         OU exclusivo bit-a-bit
~           __inv__         inversão

Sabendo manipular os operadores de maneira hábil posso obter novos resultados que antes o Python não
sabia como fazer.
"""


class Retangulo:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    # ______________________________________________________________

    def __add__(self, other):  # Somando x e y das instâncas recebidas
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)  # Retornando uma nova classe com os novos valores
    # ______________________________________________________________

    def __eq__(self, other):  # Apenas fazendo comparações entre os valores
        return self.x == other.x and self.y == other.y
    # ______________________________________________________________

    def __mul__(self, other):  # Multiplicando os valores de x e y em cada um
        return Retangulo((self.x * other.x), (self.y * other.y))
    # ______________________________________________________________

    def compara_area(self, other):  # Comparando a área de dois retângulos
        first = self.x * self.y
        second = other.x * other.y

        return first == second

########################################################################################################################


r1 = Retangulo(10, 5)
r2 = Retangulo(20, 10)
r3 = Retangulo(20, 10)
r4 = r1 + r2
r5 = r2 * r1

print(r1.x, r1.y)
print(r1 == r2)
print(r2 == r3)
print(r4.x, r4.y)
print(r4 == (r2 + r3))
print(r5.x, r5.y)
print(r2.compara_area(r3))
print(r4.x * r4.y)
print(r5.compara_area(r4))
