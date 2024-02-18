carrinho = ["carrinho", "teclado", "monitor"]
print(f"lista: {carrinho}")

print("---------- parte 1 - len() ----------")

# len() => retorna o tamanho da lista
print(f"Quantidade de itens no carrinho: {len(carrinho)}")

print("---------- parte 2 - .append ----------")

# inserindo um item no carrinho - .append
carrinho.append("mousepad")
print(f"Quantidade de itens no carrinho: {len(carrinho)}")
print(carrinho)

print("---------- parte 3 - .insert ----------")

# inserindo um item a qualquer posição - .insert
carrinho.insert(0, "fone")
print(f"Quantidade de itens no carrinho: {len(carrinho)}")
print(carrinho)

print("---------- parte 3 - .pop() ----------")

# removendo um último item - .pop
carrinho.pop
print(f"Quantidade de itens no carrinho: {len(carrinho)}")
print(carrinho)

print("---------- parte 3 - removendo um item de qualquer posição ----------")

carrinho.pop(4)
print(f"Quantidade de itens no carrinho: {len(carrinho)}")
print(carrinho)

print("---------- parte 4 - .remove() ----------")

# removendo um item em específico
carrinho.remove("monitor")
print(f"Quantidade de itens no carrinho: {len(carrinho)}")
print(carrinho)