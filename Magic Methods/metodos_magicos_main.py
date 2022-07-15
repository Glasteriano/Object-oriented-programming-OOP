from metodos_magicos_classes import *
# Prefiro chamar o nome da classe, mas como aqui será só para exemplo, não tem problema usar o *

a = A()
# ________________________________________________________

b = B()
print(type(b), '\n')
# Mostra um NoneType por não ter nada no NEW
# ________________________________________________________

c = C()
# ________________________________________________________

d = D()
print(d.nome, '\n')
# ________________________________________________________

e = E()
e.fala_oi()
# ________________________________________________________

f1 = F()
f2 = F()
f3 = F()
print(f1 == f2)
print(f2 == f3)  # Não era p'ra serem iguais, pois são instâncias diferentes
print(id(f1))
print(id(f2))  # Todas possuem o mesmo ‘id’
print(id(f3), '\n')
# ________________________________________________________

g = G()
g(1, 2, 3, navn='Sigudr')  # Não daria p'ra fazer isso nem usar o (.) chamando uma função
print()
# ________________________________________________________

h = H()
variavel = h(1, 2, 3, 4)
print(variavel)
h.hello()
# ________________________________________________________

i = I()
i.nome = 'Petr'
# print(i.nome)  # Se tentar printar êle não existe
# ________________________________________________________

j = J()
j.nome = 'Osvald'
print(j.nome, '\n')  # Executando normalmente agora
# ________________________________________________________

l = L()
l.nome = 'Fúria da Noite'
l.outro = 'Belinha'
print(l.nome)  # Valor do atributo alterado
print(l.outro, '\n')
# ________________________________________________________

m = M()
print(m)  # Posso mandar alguma informação útil quando tentarem printar a classe
print(M)  # Mostra o local de onde 'tá sendo chamado
print(M(), '\n')  # Mesma coisa que print(m)
# ________________________________________________________

n = N()
print(len(n))  # Valor alterado
