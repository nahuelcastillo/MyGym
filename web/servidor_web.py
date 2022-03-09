from flask import Flask, request, redirect, url_for, session
from flask import render_template
from web.servicios import autenticacion

app = Flask(__name__, template_folder='template')
app.secret_key = 'loginkey'

@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')

@app.route('/index')
def index2():
    return render_template('home.html')

@app.route('/logout')
def logout():
    if 'nombre' in session:
        session.pop('nombre', None)
    if 'ID' in session:
        session.pop('idusuario', None)
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not autenticacion.validar_credenciales(request.form['num'], request.form['login'], request.form['password']):
            error = 'Este usuario no existe o algun campo esta mal'
        else:
            idusuario = request.form['num']
            session['idusuario'] = idusuario
            nombre = request.form['login']
            session['nombre'] = nombre
            return redirect(url_for('homeusuario'))
    return render_template('login.html', error=error)



@app.route('/registro', methods=['GET', 'POST'])
def registro():
    error = None
    if request.method == 'POST':
        if not autenticacion.crear_usuario(request.form['num'], request.form['email'], request.form['login'], request.form['password']):
            error = 'No se pudo crear el usuario, tal vez el id ya este en uso'
        else:
            idusuario = request.form['num']
            session['idusuario'] = idusuario
            nombre = request.form['login']
            session['nombre'] = nombre
            return redirect(url_for('datosusuario'))
    return render_template('registro.html', error=error)



@app.route('/actualizarusuario', methods=['GET', 'POST'])
def actualizarusuario():
    error = None
    idusuario = session['idusuario']
    nombre = session['nombre']
    if request.method == 'POST':
        autenticacion.actualizar_usuario(idusuario, request.form['email'], request.form['login'], request.form['password'])
        nombre = request.form['login']
        session['nombre'] = nombre
        return render_template('usuariohome.html', nombre=nombre)
    return render_template('actualizarusuario.html', error=error, nombre=nombre)


@app.route('/inicio')
def inicio():
    if 'nombre' in session:
        nombre = session['nombre']
        return render_template('inicio.html', nombre=nombre)
    if not 'nombre' in session:
        return redirect(url_for('index'))



@app.route('/crearlocal', methods=['GET', 'POST'])
def crearlocal():
    error = None
    idusuario = session['idusuario']
    if request.method == 'POST':
        if not autenticacion.crearlocal(request.form['name'], request.form['direccion'], request.form['telefono'], request.form['email'], request.form['ig'], request.form['info'], idusuario):
            error = 'no se pudo crear el local'
        else:
            return redirect(url_for('listadolocal'))
    return render_template('crearlocal.html', error=error)



@app.route('/buscarlocal', methods=['GET', 'POST'])
def buscarlocal():
    error = None
    nombre = session['nombre']
    if request.method == 'POST':
        if autenticacion.obtener_local(request.form['buscar']) == 404:
            error = 'No se pudo encontrar el local'
        else:
            local = autenticacion.obtener_local(request.form['buscar'])
            reseña = autenticacion.obtener_reseña_local(request.form['buscar'])
            numero = request.form['buscar']
            session['numerobusca'] = numero
            return render_template('homelocal.html', local=local, nombre=nombre, error=error, reseña=reseña)
    return render_template('buscarLocales.html', nombre=nombre, error=error)


@app.route('/listadolocal')
def listadolocal():
    local = autenticacion.obtener_locales()
    if 'nombre' in session:
        nombre = session['nombre']
        return render_template('listadolocal.html', local=local, nombre=nombre)


@app.route('/actualizarlocal', methods=['GET', 'POST'])
def actualizarlocal():
    error = None
    if request.method == 'POST':
        local = autenticacion.actualizar_local(request.form['num'], request.form['name'], request.form['direccion'], request.form['telefono'], request.form['email'], request.form['ig'], request.form['info'])
        return render_template('actualizar.html', local=local)
    return render_template('actualizarlocal.html', error=error)

@app.route('/info')
def info():
    if 'nombre' in session:
        nombre = session['nombre']
        return render_template('infousuario.html', nombre=nombre)
    return render_template('infousuario2.html')

@app.route('/homeusuario', methods=['GET', 'POST'])
def homeusuario():
    if request.method == 'GET':
        nombre = session['nombre']
        idusuario = session['idusuario']
        dato = autenticacion.obtener_usuario_datos(idusuario)
        return render_template('usuariohome.html', dato=dato, nombre=nombre)
    return redirect(url_for('index'))

@app.route('/datosusuario', methods=['GET', 'POST'])
def datosusuario():
    error = None
    if request.method == 'POST':
        idusuario = session['idusuario']
        if not autenticacion.crear_datosusuario(idusuario, request.form['edad'], request.form['cumpl'], request.form['peso'], request.form['altura'], request.form['info']):
            error = 'no se  ingresar los datos'
        else:
            return redirect(url_for('homeusuario'))
    return render_template('datosusuario.html', error=error)


@app.route('/modificardatosusu', methods=['GET', 'POST'])
def modificardatosusu():
    error = None
    if request.method == 'POST':
        idusuario = session['idusuario']
        if not autenticacion.modificar_usuario_datos(idusuario, request.form['edad'], request.form['cumpl'], request.form['peso'], request.form['altura'], request.form['info']):
            error = 'no se pudo modificar el usuario'
        else:
            return redirect(url_for('homeusuario'))
    return render_template('datosusuario.html', error=error)


@app.route('/eliminar_local', methods=['GET', 'POST'])
def eliminar_local():
    idusuario = session['idusuario']
    if autenticacion.elimarlocal(idusuario):
        return redirect(url_for('completado'))
    return redirect(url_for('inicio'))

@app.route('/completado')
def completado():
    nombre = session['nombre']
    return render_template('deletelocal.html', nombre=nombre)

@app.route('/reseñas', methods=['GET', 'POST'])
def reseñas():
    error = None
    nombre = session['nombre']
    numero = session['numerobusca']
    if request.method == 'POST':
        if not autenticacion.crear_reseña(nombre, request.form['login'], numero):
            error = 'no se pudo crear la reseña'
        else:
            if 'numero' in session:
                session.pop('numero', None)
            return redirect(url_for('inicio'))
    return render_template('reseñas.html', error=error, numero=numero)



if __name__ == "__main__":
    app.debug = True
    app.run(port=5002)
