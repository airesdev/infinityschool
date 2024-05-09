"""connection"""
import pymysql.cursors

try:
    # connection => abre conexão com banco de dados
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='escola',
                                 cursorclass=pymysql.cursors.DictCursor)
    print('<connected>')

    # criando cursor
    cursor = connection.cursor()

except Exception as error:  # except => tipo o else; exception as error => codigo do erro
    print(f'<ERROR>: {error}')


"""funções"""
def select():
    print('-------------------------')
    sql = 'select * from alunos'  # comando
    cursor.execute(sql)  # executar
    # fetch() => separando
    alunos = cursor.fetchall()
    for aluno in alunos:  # percorrer dict
        print(f'{aluno["matricula"]}: {aluno["nome"]} \n'
              f'Nota: {aluno["nota"]} \n'
              f'Idade: {aluno["idade"]} \n'
              f'-------------------------')

def insert(nome, idade, nota, commit):
    try:
        sql = 'insert into alunos (nome, idade, nota) values (%s, %s, %s)'
        cursor.execute(sql, (nome, idade, nota))
        if commit:
            connection.commit()  # salvar no banco de dados
        print(f'<inserted>')
    except Exception as error:
        print(f'<ERROR>: {error}')

def update(nome, idade, nota, matricula, commit):
    try:
        if verif(matricula):
            sql = "update alunos set nome = %s, idade = %s, nota = %s where matricula = %s"
            cursor.execute(sql, (nome, idade, nota, matricula))
            if commit:
                connection.commit()
            print('<updated>')
        else:
            print('<notFound>')

    except Exception as erro:
        print(f'<ERROR>: {erro}')

def delete(matricula, commit):
    try:
        if verif(matricula):
            sql = "delete from alunos where matricula = %s"
            cursor.execute(sql, (matricula))
            if commit:
                connection.commit()
            print('<deleted>')
        else:
            print('<notFound>')

    except Exception as erro:
        print(f'<ERROR>: {erro}')

def verif(matricula):
    try:
        sql = 'select * from alunos where matricula = %s'
        cursor.execute(sql, matricula)
        if cursor.fetchall() == 1:
            return True
        else:
            return False
    except Exception as error:
        print(f'<ERROR>: {error}')
