from back import search

def depositar(conta: int, valor: float) -> None:
    cliente = search(conta)
    if cliente:
        cliente['saldo'] += valor
        print('deposito_realizado')
    else:
        print('notfound')