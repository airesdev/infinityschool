"""criando função"""
def aumentarSalario(salario, aumento):
    print(salario + aumento)

"""input"""
salarioUser = float(input('informe seu salario: '))
aumentoUser = float(input('informe o aumento: '))

"""chamando função"""
aumentarSalario(salarioUser, aumentoUser)