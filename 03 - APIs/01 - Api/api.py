# API - É um lugar para disponibilizar recursos ou funcionalidades
# 1 - Objetivos: nesse exemplo, vamos criar uma api que disponibiliza a consulta, criação, edição e exclusão de livros.
# 2 - URL Base: local onde será hospedado a api. No nosso caso localhost.com OBS: se você possuir um dominio, pode hospedar assim: https://medominio.com/api
# 3 - Endpoints : são os "verbos" que estarão disponíveis para a api
    # - localhost/livros/    (GET)
    # - localhost/livros/id  (GET)
    # - localhost/livros/id  (PUT)
    # - localhost/livros/id  (DELETE)
# 4 - Quais recursos : Livros
# Pré requisitos: pip3 install flask

from flask import Flask, jsonify, request

# Iniciando um app Flask
app = Flask(__name__)

#criando uma lista de dicionários. A lista começa com [] e dicionário com { : }
livros = [
    {
        'id' : 1,
        'Titulo' : 'Senhor dos aneis',
        'Autor' : 'J. R. R. Tolkien'
    },
    {
        'id' : 2,
        'Titulo' : 'Harry Potter',
        'Autor' : 'J. K. Rolland'
    },
    {
        'id' : 3,
        'Titulo' : 'James Clear',
        'Autor' : 'Hábitos Atômicos'
    }
]

# Para transformar a Funcao em APi e necessario se utlizar um decorator
@app.route('/livros' , methods = ['GET']) # methods = ['Get'] é utilizado para somente funcionar o parametro get
# Funcao obter todos
def obter_livros():
    return jsonify(livros)

# Funcao obter id
@app.route('/livros/<int:id>' , methods = ['GET'])
def obeter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
#Funcao Editar
@app.route('/livros/<int:id>' , methods = ['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
#Funcao criar
@app.route('/livros' , methods = ['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#Funcao deletar
@app.route('/livros/<int:id>' , methods = ['DELETE'])
def excuir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

# Definindo a porta e o caminho da api
app.run(port=5000, host='localhost', debug=True)