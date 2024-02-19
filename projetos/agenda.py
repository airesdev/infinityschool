agenda = {}

while True:
    options = int(input('----- Menu Inicial ----- \n'
                    '1 - Adcionar contato \n'
                    '2 - Editar contato \n'
                    '3 - Buscar contato \n'
                    '4 - Apagar contato \n'
                    '5 - Exibir agenda completa \n'
                    '6 - Sair \n'
                    'Selecione sua opção: '))

    # Adicionar contatos
    if options == 1:
        nome = input('informe o nome do contato: ')
        agenda[nome] = (input('digite o telefone: '))
        print('Contato adicionado com sucesso! \n')
    
    # Editar contato
    elif options == 2:
        nome = input('informe o nome do contato que deseja editar: ')

        # Verificando
        if nome in agenda.keys(): # Se o nome digitado estiver no dicio
            agenda[nome] = input('Digite o novo número: ')
            print('Número alterado com sucesso! \n')
        else:
            print('Contato não encontrado! \n')
    
    # Buscar contato
    elif options == 3:
        nome = input('informe o nome do contato desejado: ')

        # Verificando
        if nome in agenda.keys(): # Se o nome digitado estiver no dicio
            print(f'Contato: {nome} \n'
                  f'Telefone: {agenda[nome]} \n')
        else:
            print('Contato não encontrado! \n')
    
    # Apagar contato
    elif options == 4:
        nome = input('informe o nome do contato desejado: ')

        if nome in agenda.keys(): # Se o nome digitado estiver no dicio
            del agenda[nome]
            print('Contato deletado com sucesso! \n')

    # Exibir agenda completa
    elif options == 5:
        print(f'{agenda} \n')

    # Sair
    elif options == 6:
        break