"""Atividade #01"""
# 1. Crie uma super classe chamada veiculo, com os atributos
# marca
# modelo
# cor
# velocidadeatual = 0
# e um método abstrato chamado
# acelerar()
# 2. Crie uma subclasse chamada carro onde você vai reescrever o método acelerar()
# e este método incrementa a velocidade atual +20 cada vez que ele é chamado
#
# 3. Crie uma subclasse chamada Moto onde você vai reescrever o método acelerar()
# e este método incrementa a velocidade atual +35 cada vez que ele é chamado

from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0

    @abstractmethod
    def acelerar(self):
        pass


class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo, cor)

    def acelerar(self):
        self.velocidade += 20


class Moto(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo, cor)

    def acelerar(self):
        self.velocidade += 35


"""Prints"""
# carro = Carro('-', '-', '-')
# moto = Moto('-', '-', '-')
# print(carro.velocidade)
# carro.acelerar()
# print(carro.velocidade)
# print(moto.velocidade)
# moto.acelerar()
# print(moto.velocidade)
