from datetime import datetime
from tablasentidades.entidades.usuarios import usuarios as modelo_usuario

#este existe usuario es para registrarce
def _existe_usuario(idusuario, correoelectronico, contraseña, nombreusuario):
    usuarios = modelo_usuario.obtener_usuarios_por_nombre_clave(idusuario, correoelectronico, contraseña, nombreusuario)
    return len(usuarios) > 0

#este existe usuario es para logear
def _existe_usuario2(idusuario, contraseña, nombreusuario):
    usuarios = modelo_usuario.obtener_usuarios_por_nombre_clave2(idusuario, contraseña, nombreusuario)
    return len(usuarios) > 0

#crea una sesion en la tabla sessiones
def _crear_sesion(id_usuario):
    hora_actual = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = hora_actual.strftime("%d/%m/%Y %H:%M:%S")
    return modelo_usuario.crear_sesion(id_usuario, dt_string)

#obtiene todos los usuarios
def obtener_usuarios():
    return modelo_usuario.obtener_usuarios()

#obtiene 1 usuario por su id
def obtener_usuario(idusuario):
    usuarios = modelo_usuario.obtener_usuario(idusuario)
    if len(usuarios) == 0:
        raise Exception("El usuario no existe")
    return usuarios[0]

#crea un usuario
def crear_usuario(idusuario, correoelectronico ,nombreusuario, contraseña):
    if not _existe_usuario(idusuario, correoelectronico, nombreusuario, contraseña):
        modelo_usuario.crear_usario(idusuario, correoelectronico, nombreusuario, contraseña)
    else:
        raise Exception("El usuario ya existe")


#loguea un usuario y crea una session
def login(idusuario, contraseña, nombreusuario):
    if _existe_usuario2(idusuario, contraseña, nombreusuario):
        usuario = modelo_usuario.obtener_usuarios_por_nombre_clave2(idusuario, contraseña, nombreusuario)[0]
        return _crear_sesion(usuario['idusuario'])
    else:
        raise Exception("El usuario no existe o la clave es invalida")

#valida la session creada
def validar_sesion(id_sesion):
    sesiones = modelo_usuario.obtener_sesion(id_sesion)
    if len(sesiones) == 0:
        return False
    elif (datetime.now() - datetime.strptime(sesiones[0]['fecha_hora'], "%d/%m/%Y %H:%M:%S")).total_seconds() > 60:
        # Sesion expirada
        return False
    else:
        return True