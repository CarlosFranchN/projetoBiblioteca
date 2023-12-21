from flask import Flask,url_for,render_template,request
from markupsafe import escape
from registros import *
app = Flask(__name__)

@app.route("/")
def inicio():
    lista = Meio_dia.getCatalogo_disp()  
    # lista = ["Carlos","Franch", "Aragao"]
    return render_template("index.html", minha_lista = lista)
@app.route("/add_form", methods = ["GET","POST"])
def addForm():
    # 
    if request.method == "POST":
        tituloLivro = request.form.get("titulo")
        autorLivro = request.form.get("autor")
        Meio_dia.adicionarLivro(tituloLivro,autorLivro)
        print(f"livro {tituloLivro} foi registrado com sucesso!")
    return render_template("formAdd.html")



if __name__ == '__name__':
    app.run()