"""criando função"""
def area(base, altura):
    print(base * altura / 2)

"""input"""
baseUser = float(input('informe a base: '))
alturaUser = float(input('informe a altura: '))

"""chamando função"""
area(baseUser, alturaUser)