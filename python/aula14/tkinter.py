from tkinter import *  # Importar Tudo
from tkinter import messagebox  # Extenção
from tkinter import ttk  # Extenção

agenda = []

def Add() -> None:
    # Pegar valores
    nome = txtNome.get()
    tel = txtTel.get()
    cat = cbCat.get()

    contato = {"nome": nome, "tel": tel, "cat": cat}

    agenda.append(contato)
    messagebox.showinfo('adicionado!', 'contato adicionado com sucesso!')
    limparCampos()
    atualizarTabela()

def Edit() -> None:
    contatoSelecionado = tabela.selection()[0]
    if not contatoSelecionado:
        return
    index = tabela.index(contatoSelecionado)
    agenda[index] = {
        'nome': txtNome.get(),
        'tel': txtTel.get(),
        'cat': cbCat.get()
    }
    atualizarTabela()
    limparCampos()

def Del() -> None:
    contatoSelecionado = tabela.selection()[0]
    if not contatoSelecionado:
        return
    index = tabela.index(contatoSelecionado)
    # transformar codigo acima em função depois

    del agenda[index]
    limparCampos()
    atualizarTabela()

def limparCampos() -> None:
    txtNome.delete(0, END)
    txtTel.delete(0, END)
    cbCat.delete(0, END)

def atualizarTabela() -> None:
    # Limpar Tabela
    # get_children -> retorna uma linha com as linhas da tabela
    for linha in tabela.get_children():
        tabela.delete(linha)

    for contato in agenda:
        tabela.insert("", END, values=(contato['nome'], contato['tel'], contato['cat']))

def tabelaClique(event) -> None:
    contatoSelecionado = tabela.selection()[0]
    if not contatoSelecionado:
        return
    index = tabela.index(contatoSelecionado)

    # Preenchimento dos campos com item selecionado
    contato = agenda[index]
    limparCampos()
    txtNome.insert(0, contato['nome'])
    txtTel.insert(0, contato['tel'])
    cbCat.insert(0, contato['cat'])

"""
Elementos UI -> Funções

"""

# Elemento (Todas as funções do Tkinter começam maiúsculas)
janela = Tk()

# Adicionando Título
janela.title("Agenda Telefonica")

# Add Rótulos    (Local)  (texto)        (Cor)      (Fonte)
labelNome = Label(janela, text="Nome: ", fg="black", font="Tahoma 14 bold")
labelTel = Label(janela, text="Telefone: ", fg="black", font="Tahoma 14 bold")
labelCat = Label(janela, text="Categoria: ", fg="black", font="Tahoma 14")

# Adicionando rótulos na janela
#
# Pack <- Em ordem
#
# Place <- Específico
#
# Grid <- Em grades

labelNome.grid(row=0, column=0)
labelTel.grid(row=1, column=0)
labelCat.grid(row=2, column=0)

# Campo de Texto                         (Largura)
txtNome = Entry(janela, font="tahoma 14", width=25)
txtTel = Entry(janela, font="tahoma 14", width=25)

# Adicionando Campos na janela
txtNome.grid(row=0, column=1)
txtTel.grid(row=1, column=1)

# Botão Add                                  (Commando [Sem parênteses])
buttonAdd = Button(janela, text="Adicionar", command=Add,
                   fg="black", bg="white", font="tahoma 12", width=9, height=1)
buttonAdd.grid(row=3, column=0)

# Botão Edit
buttonEdit = Button(janela, text="Editar", command=Edit,
                    fg="black", bg="white", font="tahoma 12", width=9, height=1)
buttonEdit.grid(row=3, column=1)

# Botão Del
buttonDel = Button(janela, text="Deletar", command=Del,
                   fg="black", bg="white", font="tahoma 12", width=9, height=1)
buttonDel.grid(row=3, column=2)

# Combobox
categorias = ['amigos', 'família', 'trabalho']
cbCat = ttk.Combobox(janela, values=categorias, width=25, font='tahoma 14')
cbCat.grid(row=2, column=1)

# Tabelas -> TreeView
tabela = ttk.Treeview(janela, columns=('nome', 'tel', 'cat'), show='headings')

tabela.heading('nome', text='Nome')
tabela.heading('tel', text='Telefone')
tabela.heading('cat', text='Categoria')

# Ação para o clique no contado da tabela
tabela.bind('<ButtonRelease-1>', tabelaClique)

tabela.grid(row=4, columnspan=4)

janela.mainloop()
