print("---------- Questão 1 ----------")

lista = [10, 15, 999, 2, 6, 7, 17, 21, 350]
for i in lista:
    if i % 2 != 0:
        print("ímpar")
        lista.remove(i)
    else:
        print("par")

print(lista)

print("---------- Questão 2 ----------")

lista = [10, 15, 999, 2, 6, 7, 17, 21, 350]
maiorValor = 0
for i in lista:
    if i > maiorValor:
        maiorValor = i

print(maiorValor)

lista = [10, 15, 999, 2, 6, 7, 17, 21, 350]
userPopIndice = int(input("informe o índice do elemento que deseja remover: "))

lista.pop(userPopIndice)
print(lista)