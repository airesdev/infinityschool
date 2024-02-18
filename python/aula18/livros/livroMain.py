class Livro:
    def __init__(self, nome, id, autor, editora, ano, pags):
        self.__nome = nome
        self.__id = id
        self.__autor = autor
        self.__ano = ano
        self.__editora = editora
        self.__pags = pags
        self.__disponivel = True

    # Alt + Insert -> Options -> Getters and Setters

    def estaDisponivel(self):
        return self.__disponivel

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, value):
        self.__ano = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, value):
        self.__editora = value

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, value):
        self.__autor = value

    @property
    def pags(self):
        return self.__pags

    @pags.setter
    def pags(self, value):
        self.__pags = value

    # Tentar usar quantidade ao invés só da disponibilidade
    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print('Livro Emprestado com sucesso!')
        else:
            print('livros indiponível')

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            print('Livro devolvido ás estantes')
        else:
            print('Livro já está nas estantes')
