from flask import Flask, jsonify, render_template

app=Flask(__name__) #Framework Flask permite llamar al index.html

print('<< CONEXIÓN EN PYTHON >>') #Imprimir titulo

@app.route('/') #cuando llegue una peticion GET a traves de la raiz, va a iniciar el procedimiento llamado "home()"
def home():
    #return 0
    return render_template("index.html")# aqui se llama a nuestro HTML para ser mostrado en el buscador 
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Notas')
def Notas():
    return render_template('Notas.html')

@app.route('/Noticias')
def Noticias():
    return render_template('Noticias.html')

@app.route('/<valor>')# cuando llega la peticion GET que creamos dentro del HTML se manda a ejecutar el 
def ori(valor):               # proceso "ori(valor)" donde el valor se obtiene desde "<valor>" de la URL
    print("\n...ESPERE...TRATANDO DE RESPONDER...\n")
    
    #return 0
    return jsonify({"Respuesta": "recibí el valor en Python de: "+str(valor)})

@app.route('/Inicio')
def Inicio():
    return render_template('Inicio.html')    

# Todo el servidor junto con sus librerias ,metodos y procedimientos deberan estar antes de 
#estas dos lineas de codigo, debido a que estas echan a andar el servidor y solo lo que este antes de ellas 
# se considerara como parte del servidor.
if __name__ == '__main__':
    app.run(debug=True, port=5000)