"""criando função"""
def verif(num):
    if num % 2 == 0:
        print('Par!')
    else:
        print('Ímpar!')

"""input"""
numUser = int(input('informe o número: '))

"""chamando função"""
verif(numUser)