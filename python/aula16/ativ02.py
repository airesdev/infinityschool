"""Atividade #02"""
# 1. Crie uma classe para representar um produto e a quantidade disponível no seu estoque
# A classe produto vai conter os seguintes atributos
# -> Código
# -> Nome
# -> Preço
# -> Quantidade em estoque
#
# 2. Crie os métodos getters e setters dos atributos

class Produto:
    def __init__(self, code=0, nome='na', preco=0, qtd=0):
        self.__code = code
        self.__nome = nome
        self.__preco = preco
        self.__qtd = qtd

    def getCod(self):
        return self.__code
    def getNome(self):
        return self.__nome
    def getPreco(self):
        return self.__preco
    def getQtd(self):
        return self.__qtd
    def setCod(self, valor):
        self.__code = valor
    def setNome(self, valor):
        self.__nome = valor
    def setPreco(self, valor):
        self.__preco = valor
    def setQtd(self, valor):
        self.__qtd = valor

    def adicionar(self, valor):
        self.__qtd += valor

    def remover(self, valor):
        self.__qtd -= valor