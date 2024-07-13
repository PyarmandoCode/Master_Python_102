from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/informacion")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    #Diccionario
    datos = {
        'titulo':'Mi Pagina de Flask - Microframework',
        'descripcion':'Esta es una pagina de ejemplo usando flask',
        'items':['Elemento1','Elemento2','Elemento3']
    }
    print(datos)
    return render_template("home.html",datos=datos)


app.run(debug=True)