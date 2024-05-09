import main

while True:
    print('----- Menu inicial -----')
    print('1 - Adicionar aluno \n'
          '2 - Editar aluno \n'
          '3 - Deletar aluno \n'
          '4 - Listar alunos \n'
          '5 - Sair')
    op = int(input('Selecione uma opção: '))

    if op == 1:
        nome = input('Digite o nome do aluno: ')
        idade = input(f'Digite a idade de {nome}: ')
        nota = input(f'Digite a nota de {nome}: ')
        commit = True
        main.insert(nome, idade, nota, commit)
    elif op == 2:
        nome = input('Digite o nome do aluno: ')
        idade = input(f'Digite a idade de {nome}: ')
        nota = input(f'Digite a nota de {nome}: ')
        matricula = int(input(f'Digite a matrícula de {nome}: '))
        commit = True
        main.update(nome, idade, nota, matricula, commit)

    elif op == 3:
        matricula = int(input('Digite a matrícula do aluno: '))
        commit = True
        main.delete(matricula, commit)

    elif op == 4:
        main.select()

    elif op == 5:
        break
