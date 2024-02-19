from typing import Optional
from time import sleep

banco = [
    {'conta': 0, 'nome': 'Gabe', 'saldo': 1000.0},
    {'conta': 1, 'nome': 'Rafael', 'saldo': 950.0}
]

contaAtual = 1


def add(nome: str, saldo: float) -> None:
    global contaAtual  # Trazer uma variável global
    contaAtual += 1
    conta = {
        'conta': contaAtual,
        'nome': nome,
        'saldo': saldo
    }
    print(f'Número da conta: {contaAtual}')


def search(conta: int) -> Optional[dict or None]:
    for cliente in banco:
        if cliente['conta'] == conta:
            return cliente
    return None


def edit(conta: int, novoNome: str) -> None:
    cliente = search(conta)
    if cliente:
        cliente["nome"] = novoNome
        print('dadosalterados')
    else:
        print('notfound')


def atualizarSaldo(conta: int, novoSaldo: float):
    cliente = search(conta)
    if cliente:
        cliente["saldo"] = novoSaldo
        print('dadosalterados')
    else:
        print('notfound')


def delete(conta: int) -> None:
    cliente = search(conta)  # sempre lembrar de reutilizar funções
    if cliente:  # se houver uma conta dentro da var.
        banco.remove(cliente)
        print('clienteremovido')
    else:
        print('notfound')


def list() -> None:
    for cliente in banco:
        print(f'----- Dados do cliente {cliente["conta"]} -----\n'
              f'Nome: {cliente["nome"]}'
              f'Saldo: {cliente["saldo"]}'
              f'-----------------------------------\n')
        sleep(2)


'''
Tip:

[] - Lista

{} - Dicio

'''