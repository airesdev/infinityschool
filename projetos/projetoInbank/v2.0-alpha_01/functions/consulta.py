from back import search

def consultar(conta: int) -> None:
    cliente = search(conta)
    if cliente:
        print(cliente['saldo'])
    else:
        print('notfound')