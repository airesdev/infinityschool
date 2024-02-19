# Cadastro de Alunos
"""[ ] - Lista armazenará alunos"""
"""[ ] - Dicionário representará o aluno"""
"""[ ] - Menu com CRUD (Criar, Ler, Alterar, Deletar)"""

# Alunos -> (Lista):
"""     Aluno -> (Dicio)    """
"""     Aluno -> (Dicio)    """
"""     ...                 """

import random
alunos = []

def add(matricula, nome, curso):
    aluno = {"matricula": matricula,
             "nome": nome,
             "curso": curso}

    alunos.append(aluno)
    print('aluno cadastrado com sucesso!')
def edit(matricula, nome, curso):
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            aluno['nome'] = nome
            aluno['curso'] = curso
def search(pesquisa):
    for aluno in alunos:
        if pesquisa == aluno['matricula'] or pesquisa == aluno['nome']:
            print(f'Aluno: {aluno["nome"]} \n'
                  f'Curso: {aluno["curso"]} \n'
                  f'matricula: {aluno["matricula"]} \n')
def delete(matricula):
    for aluno in alunos:
        if matricula == aluno['matricula']:
            alunos.remove(aluno)
            print('aluno excluído com sucesso!')

while True:
    options = int(input('----- Menu Inicial ----- \n'
                        '1 - Adcionar aluno \n'
                        '2 - Buscar aluno \n'
                        '3 - Editar aluno \n'
                        '4 - Deletar aluno \n'
                        '5 - Exibir agenda completa \n'
                        '(other) - Sair \n'
                        'Selecione sua opção: '))

    # Adcionar aluno
    if options == 1:
        matricula = random.randint(1, 1000)
        nome = input('informe o nome do aluno: ')
        curso = input('informe o curso do aluno: ')
        add(matricula, nome, curso)

    # Pesquisar aluno
    elif options == 2:
        pesquisa = input('Pesquisa: ')
        search(pesquisa)

    # Editar aluno
    elif options == 3:
        matricula = int(input('informe a matrícula do aluno: '))
        nome = input('informe o novo nome do aluno: ')
        curso = input('informe o novo curso do aluno: ')
        edit(matricula, nome, curso)

    # Deletar aluno
    elif options == 4:
        matricula = int(input('informe a matrícula do aluno que deseja deletar: '))
        delete(matricula)

    # Exibir lista de alunos
    elif options == 5:
        print(f'{alunos} \n')

    else:
        break
