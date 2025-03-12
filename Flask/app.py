from flask import Flask #Aqui a classe Flask é importada da biblioteca Flask
#Criando uma instanci
app = Flask(__name__) # O argumento __name__ é usado para ajudar o Flask a localizar recursos como templates e arquivos estáticos.

@app.route("/") # é um decorator que associa a função hello_world à rota raiz ("/"). Quando alguém acessa http://127.0.0.1:5000/, o Flask chama a função hello_world
def hello_world():
    return f'Hello World'

@app.route("/about")
def about():
    return f'Pagina Sobre'

if __name__ == '__main__': #Esse bloco verifica se o script está sendo executado diretamente
    app.run(debug=True)
