from flask import Flask, request, jsonify
from tablasentidades.entidades.autenticacion import autenticacion as aut
from tablasentidades.entidades.locales import localesgym as lo
from tablasentidades.entidades.autenticacion import autenticacionloc as autl
from tablasentidades.entidades.usuarios import usuarios as us
from tablasentidades.entidades.locales import reseñas as re

app = Flask(__name__)



@app.route('/usuarios', methods=['POST'])
def crear_usario():
    datos_usuarios = request.get_json()
    if 'correoelectronico' not in datos_usuarios:
        return 'Se requiere correo electronico', 400
    if 'contraseña' not in datos_usuarios:
        return 'Se requiere contraseña', 400
    if 'nombreusuario' not in datos_usuarios or datos_usuarios['nombreusuario'] == '':
        return 'Se requiere nombre de usuario', 400
    aut.crear_usuario(datos_usuarios['idusuario'], datos_usuarios['correoelectronico'], datos_usuarios['contraseña'], datos_usuarios['nombreusuario'])
    return 'ok', 200

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(aut.obtener_usuarios())

@app.route('/usuario/<idusuario>', methods=['GET'])
def obtener_usuario(idusuario):
    try:
        usuario = aut.obtener_usuario(idusuario)
        return jsonify(usuario)
    except Exception as e:
        return 'Usuario no encontrado', 404


@app.route('/updatusuario/<idusuario>', methods=['PUT'])
def update_usuario(idusuario):
    datos_usuario = request.get_json()
    if 'correoelectronico' not in datos_usuario or datos_usuario['correoelectronico'] == '':
        return 'Se requiere correo electronico', 400
    if 'nombreusuario' not in datos_usuario or datos_usuario['nombreusuario'] == '':
        return 'Se requiere contraseña', 400
    us.update_usuario(idusuario, datos_usuario)
    return 'ok', 200


@app.route('/login', methods=['POST'])
def login():
    datos_usuarios = request.get_json()
    if 'idusuario' not in datos_usuarios:
        return 'Se requiere su id de usuario', 400
    if 'contraseña' not in datos_usuarios:
        return 'Se requiere contraseña', 400
    if 'nombreusuario' not in datos_usuarios or datos_usuarios['nombreusuario'] == '':
        return 'Se requiere nombre de usuario', 400
    try:
        id_sesion = aut.login(datos_usuarios['idusuario'], datos_usuarios['contraseña'], datos_usuarios['nombreusuario'])
        return jsonify({"id_sesion": id_sesion})
    except Exception:
        return 'USUARIO NO ENCONTRADO', 404


@app.route('/crearlocal', methods=['POST'])
def crear_local():
    datos_local = request.get_json()
    if 'nombreLocal' not in datos_local:
        return 'Se requiere nombre de local', 400
    if 'direccion' not in datos_local:
        return 'Se requiere direccion del local', 400
    if 'telefono' not in datos_local:
        return 'Se requiere telefono del local', 400
    if 'correoelectronico' not in datos_local:
        return 'se requiere correoelectronico'
    lo.crear_local(datos_local['nombreLocal'], datos_local['direccion'], datos_local['telefono'], datos_local['correoelectronico'], datos_local['instagram'], datos_local['info'], datos_local['idusuario'])
    return "ok", 200

@app.route('/eliminarlocal/<idusuario>', methods=['DELETE'])
def eliminar_local(idusuario):
    lo.eliminar_local(idusuario)
    return 'ok', 200

@app.route('/updatelocal/<idlocal>', methods=['PUT'])
def update_local(idlocal):
    datos_local = request.get_json()
    if 'nombreLocal' not in datos_local or datos_local['nombreLocal'] == '':
        return 'se requiere nombre', 400
    if 'direccion' not in datos_local or datos_local['direccion'] == '':
        return 'Se requiere direccion del local', 400
    if 'telefono' not in datos_local or datos_local['telefono'] == '':
        return 'Se requiere telefono del local', 400
    if 'correoelectronico' not in datos_local or datos_local['correoelectronico'] == '':
        return 'se requiere correoelectronico', 400
    lo.update_local(idlocal, datos_local)
    return 'ok', 200

@app.route('/locales', methods=['GET'])
def obtener_locales():
    return jsonify(autl.obtener_locales())

@app.route('/local/<nombreLocal>', methods=['GET'])
def obtener_local(nombreLocal):
    try:
        local = autl.obtener_loal(nombreLocal)
        return jsonify(local), 200
    except Exception as e:
        return 'local no encontrado', 404

@app.route('/reseña', methods=['POST'])
def crear_reseña():
    dato_reseñas = request.get_json()
    re.crear_reseña(dato_reseñas['ID_USUARIO'], dato_reseñas['reseña'], dato_reseñas['ID_LOCAL'])
    return 'ok', 200

@app.route('/obtenerreseña/<ID_LOCAL>', methods=['GET'])
def obtener_reseña(ID_LOCAL):
    try:
        datos = re.obtener_reseña_local(ID_LOCAL)
        return jsonify(datos)
    except Exception as e:
        return 'local no encontrado', 404


@app.route('/datosusuarios', methods=['POST'])
def datosusuario():
    datos_usuarios = request.get_json()
    us.crear_datosusuarios(datos_usuarios['ID'], datos_usuarios['edad'], datos_usuarios['año'], datos_usuarios['peso'], datos_usuarios['altura'], datos_usuarios['infogen'])
    return "ok", 200

@app.route('/obtenerdatosusuario/<ID>', methods=['GET'])
def obtenerdatosusuario(ID):
    try:
        datos = us.obtener_datos_usuario(ID)
        return jsonify(datos)
    except Exception as e:
        return 'local no encontrado', 404

@app.route('/modificardatosusu/<ID>', methods=['PUT'])
def modificar_datos_usuario(ID):
    datos_usuario = request.get_json()
    us.modificar_datos_usuario(ID, datos_usuario)
    return 'ok', 200


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)