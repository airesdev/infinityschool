'''Atividade'''
# 1. Crie uma classe pai chamada Conta, com os seguintes atributos
# - Numero da conta
# - Nome do cliente
# - Saldo
# e a seguinte função:
# -> depositar(valor)
#
# 2. Crie em seguida uma classe filha chamada conta corrente, com o seguinte atributo
# -> Limite do cheque especial
# e a seguinte função
# -> sacar(valor), onde o cliente pode sacar até o limite do seu cheque especial
#
# 3. Crie uma outra classe filha chamada conta poupança, com o seguinte atributo
# -> taxa de rendimento mensal
# e as seguintes funções
# sacar(valor), onde o cliente só pode sacar até o limite do saldo
# calcularRendimento()
# saldo = saldo + saldo * taxa de rendimento

class Conta:
    def __init__(self, valNum, valNome, valSaldo):
        self.num = valNum
        self.nome = valNome
        self.saldo = valSaldo

    def depositar(self, val):
        self.saldo += val

        'prints'
        print('def_depositar')
        print(self.saldo)

class contaCor(Conta):
    def __init__(self, valNum, valNome, valSaldo,
                 valLimit):

        super().__init__(valNum, valNome, valSaldo)
        self.limit = valLimit

    def sacar(self, val):
        if val < (self.saldo + self.limit):
            self.saldo -= val

            'prints'
            print('def_sacar')
            print(self.saldo)
        else:
            print('limit_reached')

class contaPoup(Conta):
    def __init__(self, valNum, valNome, valSaldo,
                 valTaxa):
        super().__init__(valNum, valNome, valSaldo)
        self.taxa = valTaxa

    def sacar(self, val):
        if val > self.saldo:
            print('limit_reached')
        else:
            self.saldo -= val

            'prints'
            print('def_sacar')
            print(self.saldo)
    def calcRendimento(self):
        self.saldo += self.saldo * self.taxa
        print(self.saldo)


'testing'
# teste1 = contaPoup(1, 'teste1', 1000, 0.1)
#
# print(teste1.saldo)
# print(teste1.nome)
# print(teste1.num)
#
# teste1.sacar(1000)
# teste1.depositar(100)
# teste1.calcRendimento()

