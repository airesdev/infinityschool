"""criando função"""
def verif(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        print('é possível formar um triângulo')
    else:
        print('não é possível formar um trângulo')

"""input"""
aUser = float(input('informe o lado A: '))
bUser = float(input('informe o lado B: '))
cUser = float(input('informe o lado C: '))

"""chamando função"""
verif(aUser, bUser, cUser)