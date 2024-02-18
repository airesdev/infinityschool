"""Questâo 01"""
# def calculo(lado: float):
#     area = lado ** 2
#     print(f'Área do quadrado: {area}cm')
# ladoUser = float(input("Informe o lado do quadrado (cm): "))
# calculo(ladoUser)

"""Questâo 02"""
# def calculo(base: float, altura: float):
#     area = (base * altura) / 2
#     print(f'Área do triângulo: {area}cm')
# base = float(input('informe a base do triângulo (cm): '))
# altura = float(input('informe a altura do triângulo (cm): '))
# calculo(base, altura)

"""Questâo 03"""
def calculo(B: float, b: float, altura: float):
    areaTrapezio = (B + b) * altura / 2
    print(f'Área do Trapézio: {areaTrapezio}cm')
B = float(input('informe a base maior do trapézio (cm): '))
b = float(input('informe a base menor do trapézio (cm): '))
altura = float(input('informe a altura do trapézio (cm): '))
calculo(B, b, altura)