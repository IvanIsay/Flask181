#importacion del framework
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

#Inicializacion del APP
app= Flask(__name__)

#Configuracion de la conexion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbflask'
app.secret_key='mysecretkey'
mysql= MySQL(app)

# declaracion de rutas

# Ruta principal /  http://localhost:5000
@app.route('/')
def index():
    CC= mysql.connection.cursor();
    CC.execute('select * from albums')
    conAlbums= CC.fetchall()
    
    return render_template('index.html',listAlbums= conAlbums)


# ruta http:localhost:5000/guardar - tipo POST para Insert

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
        
        # pasamos a variables el contenido de los input
        Vtitulo= request.form['txtTitulo']
        Vartista= request.form['txtArtista']
        Vanio= request.form['txtAnio']
        
        #Conectar y ejecutar el insert
        CS= mysql.connection.cursor()
        CS.execute('insert into albums(titulo,artista,anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio))
        mysql.connection.commit()
    
    flash('El album fue agregado correctamente')    
    return redirect(url_for('index'))



@app.route('/editar/<id>')
def editar(id):
    cursoId= mysql.connection.cursor()
    cursoId.execute('select * from albums where id= %s',(id,))
    consulId= cursoId.fetchone()
    print(consulId)
    return render_template('editarAlbum.html',album = consulId)

app.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    
    if request.method == 'POST':
        varTitulo= request.form['txtTitulo']
        varArtist= request.form['txtArtista']
        varAnio= request.form['txtAnio'] 
        
        curAct= mysql.connection.cursor()
        curAct.execute('update albums set titulo= %s,artista= %s, anio= %s where id= %s',(varTitulo,varArtist,varAnio,id))
        mysql.connection.commit()
        
    flash('Se actualizo el Album'+ varTitulo)
    return redirect(url_for('index'))











@app.route('/eliminar')
def eliminar():
    return " Se Elimino en la BD" 






#ejecucion del Servidor en el Puerto 5000
if __name__ == '__main__':
    app.run(port=5000,debug=True)
    
    