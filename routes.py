from flask import Flask, request
import sys
#Importa caminho da Home#
from pathlib import Path
#Seta o caminho da Home#
home = str(Path.home())
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Paths para os IDS#
sys.path.insert(1, home + '/Documents/Api-Control/IdGenerator/')
#importa a funcao de gerar ID
from idgenerator import gerador_id, gerar_uuid

app = Flask("Main Page")

@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():
    #Itens para post#
    post = {"id": gerador_id(),
            "UUID": gerar_uuid()}
    return post

app.run()
