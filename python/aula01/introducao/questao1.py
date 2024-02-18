"""criando função"""
def imc(peso, altura):
    print(peso / altura ** 2)

"""input"""
userPeso = float(input('informe seu peso: '))
userAlt = float(input('informe sua altura: '))

"""chamando função"""
imc(userPeso, userAlt)