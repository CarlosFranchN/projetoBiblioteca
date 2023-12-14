from livro import * 
from membros import *
from biblioteca import *

livro1 = Livro(titulo="Dune", autor="Frank Herbert",id=1,status="DISPONIVEL")
livro2 = Livro(titulo="O Senhor dos Anéis",autor="J.R.R Tolkien", id=2, status="DISPONIVEL")
livro3 = Livro(titulo="O Grande Gatsby",autor="F. Scott Fitzgerald",id=3, status="DISPONIVEL")
livro4 = Livro(titulo="Pequeno Principe",autor="Antoine de Saint-Exupéry",id=4, status="DISPONIVEL")
livro5 = Livro(titulo="Morro dos Ventos Uivantes",autor="Emily Brontê",id=5,status="DISPONIVEL")
lista_livros = [livro1,livro2,livro3,livro4,livro5]

membro1 = Membro(nome="Carlos Franch", num_membro=1)
membro2 = Membro(nome="Mariana Aragao", num_membro=2)
membro3 = Membro(nome="Johnny Bravo", num_membro=3)
lista_membros = [membro1,membro2,membro3]

Meio_dia = Biblioteca(catalogo_disp=[], membros=[])

for livro in lista_livros:
    Meio_dia.catalogo_disp.append(livro)
for membro in lista_membros:
    Meio_dia.membros.append(membro)

# print(Meio_dia.catalogo_disp)
# print(Meio_dia.membros)
