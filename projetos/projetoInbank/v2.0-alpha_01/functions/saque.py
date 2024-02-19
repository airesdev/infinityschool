from back import search

def sacar(conta: int, valor: float) -> None:
    cliente = search(conta)
    if cliente:
        if cliente['saldo'] >= valor:
            cliente['saldo'] -= valor
            print('saque_realizado')
        else:
            print('insuficiente')
    else:
        print('notfound')