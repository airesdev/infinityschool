from livroMain import Livro


class LivroDigital(Livro):
    def __init__(self, nome, id, autor, editora, ano, pags, tipo):
        super().__init__(nome, id, autor, editora, ano, pags)
        self.__tipo = tipo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, value):
        self.__tipo = value
