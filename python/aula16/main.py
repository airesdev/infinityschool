'relembrando'
# # class => modelo
# class Aluno:
#
#     # método CONSTRUTOR
#     def __init__(self, valNome, valCurso, valMat):
#
#         # criando ATRIBÚTOS
#         self.nome = valNome
#         self.curso = valCurso
#         self.mat = valMat
#         self.pont = None
#         self.falt = 0
#
#     # MÉTODOS
#     def altNome(self, newNome):
#         self.nome = newNome
#         print(self.nome)
#     def altCurso(self, newCurso):
#         self.curso = newCurso
#         print(self.curso)
#     def altFalt(self, qtd):
#         self.falt += qtd
#         print(self.falt)
#     def altPont(self, newPont):
#         self.pont = newPont
#         print(self.pont)
#     def results(self):
#         if self.pont is None:
#             print('_NONE_')
#             return
#         if self.pont >= 6:
#             print('_APROVADO_')
#         else:
#             print('_REPROVADO_')
#
#
# # criando OBJ.
# aluno1 = Aluno('Jonas', "Typescript", 1)
#
# '''prints'''
# # print(aluno1.nome)
# # print(aluno1.mat)
# # print(aluno1.curso)
# # print(aluno1.pont)

'herança'


# criando CLASSE PAI
class Funcionario:
    def __init__(self, valMat, valNome, valSal):
        self.mat = valMat
        self.nome = valNome
        self.sal = valSal

    def exibirDados(self):
        print('----- Dados -----\n'
              f'Funcionário: {self.nome}\n'
              f'Matrícula: {self.mat}\n'
              f'Salário: {self.sal}\n')


# SUBCLASSES
class Gerente(Funcionario):
    ...
    # def __init__(self, valMat, valNome, valSal,
    #              valMeta, valComis):
    #
    #     # chamando classe pai
    #     super().__init__(valMat, valNome, valSal)
    #
    #     self.meta = valMeta
    #     self.comis = valComis
    #
    #     # note to self: see if there's an easier way of creating such classes


class Vendedor(Funcionario):
    def __init__(self, valMat, valNome, valSal,
                 valMeta, valComis):
        # chamando classe pai
        super().__init__(valMat, valNome, valSal)

        self.meta = valMeta
        self.comis = valComis

    def exibirDados(self):
        super().exibirDados()
        print(f'meta do mês: {self.meta}')
        print(f'meta do comissão: {self.comis}')

        # note to self: see if there's an easier way of creating such classes


class Contador(Funcionario):
    ...
    # def __init__(self, valMat, valNome, valSal,
    #              valMeta, valComis):
    #     # chamando classe pai
    #     super().__init__(valMat, valNome, valSal)
    #
    #     self.meta = valMeta
    #     self.comis = valComis
    #
    #     # note to self: see if there's an easier way of creating such classes


'prints'
# teste2 = Vendedor(1, 'teste2', 2, 3, 4)

# print(teste.nome)
# print(teste.mat)
# print(teste.sal)
# print(teste.meta)
# print(teste.comis)
