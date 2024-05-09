from livros.livroFisico import LivroFisico
# from livros.livroDigital import LivroDigital
from membros.membro import Membro


class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__membros = []

    def cadastrarMembro(self, membro: Membro):
        self.__membros.append(membro)
        print('Novo membro adicionado')

    def deletarMembro(self, id):
        for membro in self.__membros:
            if membro.id == id:
                self.__membros.remove(membro)
                print('Membro deletado com sucesso')

    def cadastrarLivro(self, livro: LivroFisico):
        self.__livros.append(livro)
        print('Novo livros adicionado')

    def deletarLivro(self, id):
        for livro in self.__livros:
            if livro.id == id:
                self.__livros.remove(livro)
                print('Livro deletado com sucesso')

    def listarLivros(self):
        print('----- Livros Cadastrados -----')
        for livro in self.__livros:
            print(f'----- Dados -----')
            print(f'Id: {livro.id}')
            print(f'Nome: {livro.nome}')
            print(f'Autor: {livro.autor}')
            print(f'Ano: {livro.ano}')
            print(f'Págs: {livro.pags}')

    def listarMembros(self):
        pass


if __name__ == '__main__':
    biblioteca = Biblioteca()
    membro01 = Membro('m-01', 1, 'na', 'na')
    membro02 = Membro('m-02', 2, 'na', 'na')
    livro01 = LivroFisico('l-01', 1, 'na', 'na', 0, 0, 'na')
    livro02 = LivroFisico('l-02', 2, 'na', 'na', 0, 0, 'na')
    biblioteca.cadastrarMembro(membro01)
    biblioteca.cadastrarMembro(membro02)
    biblioteca.cadastrarLivro(livro01)
    biblioteca.cadastrarLivro(livro02)
    biblioteca.listarMembros()
    biblioteca.listarLivros()
