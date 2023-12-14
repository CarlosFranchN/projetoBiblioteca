
class Membro():
    def __init__(self,nome,num_membro):
        self.nome = nome
        self.num_membro = num_membro
        self.historico = []

    def adicionar_livro(self,livro):
        self.historico.append(livro)
