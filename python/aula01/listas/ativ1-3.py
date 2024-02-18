print("---------- Questão 1 ----------")

lista = []
for i in range(3):
    userProduto = input("informe o produto: ")
    lista.append(userProduto)

print(lista)

print("---------- Questão 2 ----------")

lista = []
quantidade = 3 # tentar usar input depois!!!
for i in range(quantidade):
    userNota = float(input("informe a nota: "))
    lista.append(userNota)

media = (lista[0] + lista[1] + lista[2]) / len(lista)
print(round(media, 2))
 
print("---------- Questão 3 ----------")

lista = []
quantidade = 10
maiorValor = 0

for i in range(quantidade):
    userValor = float(input(f"informe um número ({i + 1}/{quantidade}): "))
    if userValor > maiorValor:
        maiorValor = userValor
lista.append(userValor)

print(maiorValor)