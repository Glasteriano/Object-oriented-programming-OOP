from classe_abstrata_classes import ContaCorrente, ContaPoupanca

cp = ContaPoupanca(1111, 2222, 0)

cp.depositar(100)
cp.sacar(70)
print(cp.saldo)
print(cp.conta)
print(cp.agencia)
print('_________________________________\n')

cc = ContaCorrente(agencia=1111, conta=3333, saldo=100, limite=200)

cc.depositar(500)
print(cc.saldo)
print(cc.conta)
print(cc.agencia)
