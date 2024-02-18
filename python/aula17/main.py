"""Relembrando"""
# class Conta:
#     def __init__(self, conta, cliente):
#         self.conta = conta
#         self.cliente = cliente
#         self.saldo = 0
#
#     def print(self):
#         print(f'Seu saldo: {self.saldo}')
#
#     def deposito(self, valor):
#         self.saldo += valor
#         print('Deposito realizado!')
#
#     def sacar(self, valor):
#         if self.saldo >= valor:
#             self.saldo -= valor
#             print('Saque realizado.')
#         else:
#             print('Saldo insuficiente.')
#
#
# class ContaPoupanca(Conta):
#     def __init__(self, conta, cliente, rendimentos):
#         super().__init__(conta, cliente)
#         self.rendimentos = rendimentos
#
#     def calcularRendimentos(self):
#         self.saldo = self.saldo + (self.saldo * self.rendimentos)
#         print('rendimentos calculados com sucesso!')
#
#
# class ContaCorrente(Conta):
#     def __init__(self, conta, cliente, limite):
#         super().__init__(conta, cliente)
#         self.limite = limite
#
#     # sobrescrevendo função sacar
#     def sacar(self, valor):
#         if self.saldo + self.limite >= valor:
#             self.saldo -= valor
#             print(f'Saque realizado.')
#         else:
#             print('Saldo insuficiente.')
#
#
# 'prints'
# # ph = ContaCorrente(1, "Gabe", 100)
# # ph.print()
# # ph.deposito(50)
# # ph.print()
# # ph.sacar(25)
# # ph.sacar(200)
# # ph.print()
# # print("-" * 50)

"""Polimorfismo"""
# class Passaro:
#
#     #método Abstrato
#     def cantar(self):
#         return 'cantar'
#
# class BemTeVi(Passaro):
#     def cantar(self):
#         return 'bem_te_vi'
#
# class PicaPau(Passaro):
#     def cantar(self):
#         return 'HEHEHEHEHE! HEHEHEHEHE! HEHEHEHEHEHEHEHE!'
#
# bemTeVi = BemTeVi()
# picaPau = PicaPau()
# print(bemTeVi.cantar())
# print(picaPau.cantar())

"""Encapsulamento"""
# class Conta:
#     def __init__(self, conta, cliente):
#         self.__conta = conta
#         self.__cliente = cliente
#         self.__saldo = 0
#
#     # Métodos acessores
#     # getters e setters
#     def getSaldo(self):
#         return self.__saldo
#
#     def setSaldo(self, valor):
#         self.__saldo = valor
#
#     def getConta(self):
#         return self.__conta
#
#     def setConta(self, valor):
#         self.__conta = valor
#
#     def getCliente(self):
#         return self.__cliente
#
#     def setCliente(self, valor):
#         self.__cliente = valor

