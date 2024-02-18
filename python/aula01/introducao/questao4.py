"""criando função"""
def area(baseMaior, baseMenor, altura):
    print((baseMaior + baseMenor) * altura / 2)

"""input"""
baseMaiorUser = float(input('informe a base maior: '))
baseMenorUser = float(input('informe a base menor: '))
alturaUser = float(input('informe a altura: '))

"""chamando função"""
area(baseMaiorUser, baseMenorUser, alturaUser)
