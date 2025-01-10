from flask import Flask #Aqui estou importando Flask da biblioteca Flask

#Criação da aplicação
app = Flask(__name__) #A variavel app é uma instacia da classe Flask

#Definindo Rotas
@app.route("/") #As rotas são as URLs que a aplicação web suporta. Aqui estão as rotas definidas:
def hello_world():#O decorador @app.route("/") associa a URL raiz (/) à função hello_world.
    return "Hello World!"

@app.route("/about")
def about():
    return "Página Sobre"

#Execução da Aplicação
if __name__ == '__main__':
    app.run(debug=True)#O método app.run() inicia o servidor web do flask e o parâmetro debug=True ativa o modo de depuração
