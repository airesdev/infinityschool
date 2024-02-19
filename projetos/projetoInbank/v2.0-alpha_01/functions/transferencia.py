from back import search

def transferir(c_origin: int, c_destination: int, valor: float):
    origem = search(c_origin)
    destino = search(c_destination)
    if origem and destino:
        if origem >= valor:
            destino['saldo'] += valor
            origem['saldo'] -= valor
            print('success')
        else:
            print('insuficiente')
    else:
        print('notfound')