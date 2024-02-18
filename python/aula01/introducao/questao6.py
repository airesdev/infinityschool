"""criando função"""
def verif(a, b, c):
    if a == b and b == c and c == a:
        print("equilatero!")
    elif a == b or b == c or c == a:
        print("isóceles!")
    else:
        print("escaleno!")

"""input"""
aUser = float(input('informe o lado A: '))
bUser = float(input('informe o lado B: '))
cUser = float(input('informe o lado C: '))

"""chamando função"""
verif(aUser, bUser, cUser)
