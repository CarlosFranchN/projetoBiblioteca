class Livro():
    def __init__(self,titulo, autor, id,status):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.status = status
        # DISPONIVEL e INDISPONIVEL

    def get_infos(self):
        return f"Titulo: {self.titulo} , Autor: {self.autor}, Id:{self.id}, Status: {self.status}"