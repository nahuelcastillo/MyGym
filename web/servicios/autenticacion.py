import requests

from web.servicios import rest_api


def validar_credenciales(idusuario, nombreusuario, contraseña,):
    body = {"idusuario": idusuario,
            "nombreusuario": nombreusuario,
            "contraseña": contraseña}
    respuesta = requests.post(f'{rest_api.API_URL}/login', json=body)
    return respuesta.status_code == 200


def crear_usuario(idusuario, correoelectronico, nombreusuario, contraseña,):
    body = {"idusuario": idusuario,
            "correoelectronico": correoelectronico,
            "nombreusuario": nombreusuario,
            "contraseña": contraseña}
    respuesta = requests.post(f'{rest_api.API_URL}/usuarios', json=body)
    return respuesta.status_code == 200


def obtener_usuarios():
    respuesta = requests.get(f'{rest_api.API_URL}/usuarios')
    return respuesta.json()


def obtener_usario(idusuario):
    respuesta = requests.get(f'{rest_api.API_URL}/usuarios/{idusuario}')
    return respuesta.json()


def crearlocal(nombreLocal, direccion, telefono, correoelectronico, instagram, info, idusuario):
    body = {"nombreLocal": nombreLocal,
            "direccion": direccion,
            "telefono": telefono,
            "correoelectronico": correoelectronico,
            "instagram": instagram,
            "info": info,
            "idusuario": idusuario
            }
    respuesta = requests.post(f'{rest_api.API_URL}/crearlocal', json=body)
    return respuesta.status_code == 200


def obtener_local(nombreLocal):
    respuesta = requests.get(f'{rest_api.API_URL}/local/{nombreLocal}')
    if respuesta.status_code == 404:
        return 404
    else:
        return respuesta.json()


def obtener_locales():
    respuesta = requests.get(f'{rest_api.API_URL}/locales')
    return respuesta.json()


def actualizar_local(idlocal, nombreLocal, direccion, telefono, correoelectronico, instagram, info):
    body = {"nombreLocal": nombreLocal,
            "direccion": direccion,
            "telefono": telefono,
            "correoelectronico": correoelectronico,
            "instagram": instagram,
            "info": info}
    respuesta = requests.put(f'{rest_api.API_URL}/updatelocal/{idlocal}', json=body)
    return respuesta.status_code == 200


def actualizar_usuario(idusuario, correoelectronico, nombreusuario, contraseña):
    body = {"correoelectronico": correoelectronico,
            "nombreusuario": nombreusuario,
            "contraseña": contraseña}
    respuesta = requests.put(f'{rest_api.API_URL}/updatusuario/{idusuario}', json=body)
    return respuesta.status_code == 200

def crear_datosusuario(ID, edad, año, peso, altura, infogen):
    body = {"ID": ID,
            "edad": edad,
            "año": año,
            "peso": peso,
            "altura": altura,
            "infogen": infogen}
    respuesta = requests.post(f'{rest_api.API_URL}/datosusuarios', json=body)
    return respuesta.status_code == 200

def obtener_usuario_datos(ID):
    respuesta = requests.get(f'{rest_api.API_URL}/obtenerdatosusuario/{ID}')
    return respuesta.json()

def modificar_usuario_datos(ID, edad, año, peso, altura, infogen):
    body = {"edad": edad,
            "año": año,
            "peso": peso,
            "altura": altura,
            "infogen": infogen}
    respuesta = requests.put(f'{rest_api.API_URL}/modificardatosusu/{ID}', json=body)
    return respuesta.status_code == 200

def elimarlocal(idusuario):
    respuesta = requests.delete(f'{rest_api.API_URL}/eliminarlocal/{idusuario}')
    return respuesta.status_code == 200

def crear_reseña(ID_USUARIO, reseña, ID_LOCAL):
    body = {"ID_USUARIO": ID_USUARIO,
            "reseña": reseña,
            "ID_LOCAL": ID_LOCAL}
    respuesta = requests.post(f'{rest_api.API_URL}/reseña', json=body)
    return respuesta.status_code == 200

def obtener_reseña_local(ID_LOCAL):
    respuesta = requests.get(f'{rest_api.API_URL}/obtenerreseña/{ID_LOCAL}')
    if respuesta.status_code == 404:
        return 404
    else:
        return respuesta.json()
