from flask import Flask, flash, render_template, request, session, json, jsonify
import os
import re

app = Flask(__name__)

@app.route('/', methods=['GET'])

def apilibro():
    doc_name = request.args.get('doc_name')
    term = request.args.get('term')

    workdir = "C:\libros\\"
    
    #abrir el archivo seleccionado y guardarlo en un string
    file = open(workdir+doc_name, "r",encoding='utf-8')
    string = file.read()

    #pasar todo a minúscula
    lower_string = string.lower()

    #remover todos los números
    no_number_string = re.sub(r'\d+','',lower_string)

    #remover signos de puntuación
    no_punc_string = re.sub(r'[^\w\s]','', no_number_string)

    #remover espacios
    no_wspace_string = no_punc_string.strip()

    #separar en términos
    lst_string = no_wspace_string.split()

    #buscar una palabra específica y contarla
    lst_string = lst_string.count(term)

    #return "{ 'frecuencia' :  
    return jsonify({"frecuencia": lst_string})

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=False)
