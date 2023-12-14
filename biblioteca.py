from livro import *
from membros import *

class Biblioteca():
    def __init__(self,catalogo_disp,membros):
        self.catalogo_disp = []
        self.membros = []
        self.catalogo_livros = self.catalogo_disp

    def adicionarLivro(self,titulo, autor):
        newId = self.catalogo_disp[-1].id + 1
        newStatus = "DISPONIVEL"
        newLivro = Livro(titulo=titulo,autor=autor,id=newId,status=newStatus)
        self.catalogo_disp.append(newLivro)
        return "Livro cadastrado com sucesso!!"

    def cadastroMembro(self,membro):
        newNum = self.membros[-1].num_membro + 1
        newMembro = Membro(nome=membro,num_membro=newNum)
        self.membros.append(newMembro)

    def pesquisa(self,livro_pesquisado):
        for livro in self.catalogo_livros: 
            if livro_pesquisado == livro.titulo:
                return f"O livro {livro.titulo} esta registrado"
            else:
                return f"NÃO HÁ ESTE LIVRO NOS REGISTROS"
            
    def emprestimo(self,livro_emprestado,membro):
        for livro in self.catalogo_disp:
            if livro.titulo == livro_emprestado and livro.status == "DISPONIVEL":
                livro.status = "INDISPONIVEL"
                for persona in self.membros:
                    if persona.nome == membro:
                        persona.historico.append(livro_emprestado)
                return "Livro emprestado com sucesso"
            else:
                return "O livro esta INDISPONIVEL"
            
    def devolucao(self,livro):
        for livro_atual in self.catalogo_disp:
            if livro_atual.titulo == livro:
                livro_atual.status = "DISPONIVEL"
                return f"O livro {livro} foi devolvido"
            else: 
                return f"Nao pode ser devolvido"
    def lista(self):
        for livro in self.catalogo_disp:
            if livro.status == "DISPONIVEL":
                print(livro.get_infos())
    def listarMembros(self):
        for membro in self.membros:
            print(membro.nome)
    def info(self, livro):
        for livro_atual in self.catalogo_disp:
            if livro_atual.titulo == livro:
                return livro_atual.get_infos()
    def historico_membro(self, nome):
        for membro_atual in self.membros:
            if membro_atual.nome == nome:
                print(membro_atual.nome, membro_atual.historico)


            