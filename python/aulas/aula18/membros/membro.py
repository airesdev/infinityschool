from livros.livroFisico import LivroFisico


# from livros.livroDigital import LivroDigital


class Membro:
    def __init__(self, nome, id, endereco, telefone):
        self.__nome = nome
        self.__id = id
        self.__endereco = endereco
        self.__telefone = telefone
        self.__livros = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, value):
        self.__telefone = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def livros(self):
        return self.__livros

    @livros.setter
    def livros(self, value):
        self.__livros = value

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, value):
        self.__endereco = value

    def emprestarLivro(self, livro: LivroFisico):
        if livro.estaDisponivel():
            self.__livros.append(livro)
            livro.emprestar()
        else:
            print('Livro indisponível')

    def devolverLivro(self, livro: LivroFisico):
        if not livro.estaDisponivel():
            self.__livros.remove(livro)
            livro.devolver()
        else:
            print('Livro não encontrado')
