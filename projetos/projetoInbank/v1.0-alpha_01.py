cliente = {}
import random
def Verif(senha):
    pass

# def addCliente(nome, num, senha):
#     cliente = {"nome": nome,
#                "senha": senha,
#                "número": num}
#     return cliente

while True:

    opcao = int(input("------- Menu inicial ------- \n"
                      "1 - Adicionar Cliente \n"
                      "2 - Editar Cliente \n"
                      "3 - Consultar conta \n"
                      "4 - Deletar cliente \n"
                      "5 - Exibir todos os clientes \n"
                      "6 - Sacar dinheiro \n"
                      "7 - Depositar dinheiro \n"
                      "8 - Transferir dinheiro \n"
                      "Selecione sua opção: "))
    if opcao == 1:
        nome = input('Digite seu nome: ')
        cliente["nome"] = nome
        senha = input('Digite a sua senha: ')
        cliente["senha"] = senha
        num = random.randint(1, 20)
        cliente["num"] = num
        saldo = 0
        cliente["saldo"] = saldo
        # addCliente(nome, senha, num)
        print(f"número da sua conta: {num}")
        print(cliente)

    elif opcao == 2:
        nome = input('Digite o nome do contato: ')
        if nome in cliente.keys():
            cliente[nome] = input('Digite a nova senha: ')
            print('Dados alterados com sucesso!')
        else:
            print('Contato não encontrado!')

    elif opcao == 3:
        nome = input('Digite o nome: ')
        senha = input('Digite a senha: ')
        if nome and senha in cliente.values():
            print(f"Número do cliente: {cliente[num]}")
            print(f"Saldo do cliente: {cliente[saldo]}")
        else:
            print("Contato não encontrado!")

    elif opcao == 4:
        nome = input('Digite o nome: ')
        senha = input('Digite a senha: ')
        if nome and senha in cliente.keys():
            del cliente[nome]
            print('Contato excluído com sucesso!')
        else:
            print('Contato não encontrado!')

    elif opcao == 5:
        print(cliente)

    elif opcao == 6:
        nome = input('Digite o nome: ')
        senha = input('Digite a senha: ')
        num = input('Digite o número: ')
        if nome and senha and num in cliente.keys():
            print(f'Saldo disponivel para saque: {cliente[saldo]}')
            if cliente[saldo] > 0:
                saque = float(input("Informe o valor que deseja sacar: "))
                if saque > cliente[saldo]:
                    print(f'Saldo indisponível')
                    break
                else:
                    cliente[saldo] -= saque
                    print(f'Saldo disponivel: {cliente[saldo]}')
        else:
            print('Contato não encontrado!')

    elif opcao == 7:
        nome = input('Digite o nome: ')
        if nome in cliente.values():
            deposito = float(input('digite o valor que deseja depositar: '))
            cliente[saldo] = saldo + deposito
            print(f'Seu saldo atual é: {cliente[saldo]}')
        else:
            print('Contato não encontrado!')



    elif opcao == 9:
        break