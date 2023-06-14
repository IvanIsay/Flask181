#importacion del framework
from flask import Flask
from flask_mysqldb import MySQL

#Inicializacion del APP
app= Flask(__name__)

#Configuracion de la conexion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbflask'
mysql= MySQL(app)

# declaracion de rutas

# Ruta principal /  http://localhost:5000
@app.route('/')
def index():
    return "Hola Mundo FLASK"

@app.route('/guardar')
def guardar():
    return "Se guardo en la BD"

@app.route('/eliminar')
def eliminar():
    return " Se Elimino en la BD" 



#ejecucion del Servidor en el Puerto 5000
if __name__ == '__main__':
    app.run(port=5000,debug=True)
    
    