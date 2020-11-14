from flask import Flask, request
import sys
#Importa caminho da Home#
from pathlib import Path
#Seta o caminho da Home#
home = str(Path.home())
print(home)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Paths para os IDS#
sys.path.insert(1, home + '/Documents/Api-Control/IdGenerator/')
#importa a funcao de gerar ID
from idgenerator import gerador_id

app = Flask("Main Page")

@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return {"ola" : "mundo"}

@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():
    return {"id": gerador_id()}


app.run()
