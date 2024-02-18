from livroMain import Livro


class LivroFisico(Livro):
    def __init__(self, nome, id, autor, editora, ano, pags, capa):
        super().__init__(nome, id, autor, editora, ano, pags)
        self.__capa = capa

    @property
    def capa(self):
        return self.__capa

    @capa.setter
    def capa(self, value):
        self.__capa = value
