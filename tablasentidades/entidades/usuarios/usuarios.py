from tablasentidades.tablas.conexionbd import basedatos

def crear_usario(idusuario, correoelectronico, contraseña, nombreusuario):
    crear_usuario_sql = f"""
        INSERT INTO Usuario (idusuario, correoelectronico, contraseña, nombreusuario)
        VALUES ('{idusuario}','{correoelectronico}','{contraseña}','{nombreusuario}')
    """
    bd = basedatos()
    bd.ejecutar_sql(crear_usuario_sql)

def obtener_usuario(idusuario):
    obtener_usuarios_sql = f"""
        SELECT idusuario, correoelectronico, contraseña, nombreusuario
        FROM Usuario 
        WHERE idusuario = {idusuario}
    """
    bd = basedatos()
    return [{"idusuario": filas[0],
             "correoelectronico": filas[1],
             "contraseña": filas[2],
             "nombreusuario": filas[3]
             } for filas in bd.ejecutar_sql(obtener_usuarios_sql)]


def obtener_usuarios():
    obtener_usuarios_sql = f"""
        SELECT idusuario, correoelectronico, contraseña, nombreusuario
        FROM Usuario 
    """
    bd = basedatos()
    return [{"idusuario": registro[0],
             "correoelectronico": registro[1],
             "contraseña": registro[2],
             "nombreusuario": registro[3]
             } for registro in bd.ejecutar_sql(obtener_usuarios_sql)]

def crear_sesion(id_usuario, dt_string):
    crear_sesion_sql = f"""
               INSERT INTO Sesiones(ID_USUARIO, FECHA_HORA)
               VALUES ('{id_usuario}', '{dt_string}')
           """
    bd = basedatos()
    return bd.ejecutar_sql(crear_sesion_sql, True)

def obtener_sesion(id_sesion):
    obtener_sesion_sql = f"""
        SELECT ID, ID_USUARIO, FECHA_HORA FROM SESIONES WHERE ID = {id_sesion}
    """
    bd = basedatos()
    return [{"id": registro[0],
             "id_usuario": registro[1],
             "fecha_hora": registro[2]}
            for registro in bd.ejecutar_sql(obtener_sesion_sql)]


#este obtener usuario por nombre clave es para registrarce
def obtener_usuarios_por_nombre_clave(idusuario, correoelectronico, contraseña, nombreusuario):
    obtener_usuario_sql = f"""
            SELECT idusuario, correoelectronico, contraseña, nombreusuario 
            FROM Usuario 
            WHERE idusuario='{idusuario}' and correoelectronico='{correoelectronico}' and contraseña='{contraseña}' and nombreusuario='{nombreusuario}'
        """
    bd = basedatos()
    return [{"idusuario": registro[0],
             "correoelectronico": registro[1],
             "contraseña": registro[2],
             "nombreusuario": registro[3]
             } for registro in bd.ejecutar_sql(obtener_usuario_sql)]

#este obtener usuario por nombre clave es para logear
def obtener_usuarios_por_nombre_clave2(idusuario, contraseña, nombreusuario):
    obtener_usuario_sql = f"""
            SELECT idusuario, correoelectronico, contraseña, nombreusuario 
            FROM Usuario 
            WHERE  idusuario='{idusuario}' and contraseña='{contraseña}' and nombreusuario='{nombreusuario}'
        """
    bd = basedatos()
    return [{"idusuario": registro[0],
             "correoelectronico": registro[1],
             "contraseña": registro[2],
             "nombreusuario": registro[3]
             } for registro in bd.ejecutar_sql(obtener_usuario_sql)]

def update_usuario(idusuario, datos_usuario):
    update_local_sql = f"""
            UPDATE Usuario 
            SET correoelectronico='{datos_usuario['correoelectronico']}', contraseña='{datos_usuario['contraseña']}', nombreusuario='{datos_usuario['nombreusuario']}' 
            WHERE idusuario='{idusuario}' 
            """
    db = basedatos()
    db.ejecutar_sql(update_local_sql)

#se conecta con la tabla datosusuarios y crea los datos del usuario
def crear_datosusuarios(ID, edad, año, peso, altura, infogen):
    crear_datosusuarios_sql = f"""
        INSERT INTO datosusuario (ID, edad, año, peso, altura, infogen)
        VALUES ('{ID}','{edad}','{año}','{peso}','{altura}','{infogen}')
    """
    bd = basedatos()
    bd.ejecutar_sql(crear_datosusuarios_sql)

#datos usuario obtener por id del usuario
def obtener_datos_usuario(ID):
    obtener_datos_usuario_sql = f"""
        SELECT ID, edad, año, peso, altura, infogen
        FROM datosusuario 
        WHERE ID = {ID}
    """
    bd = basedatos()
    return [{"ID": filas[0],
             "edad": filas[1],
             "año": filas[2],
             "peso": filas[3],
             "altura": filas[4],
             "infogen": filas[5]
             } for filas in bd.ejecutar_sql(obtener_datos_usuario_sql)]

#modificar datos del usuario
def modificar_datos_usuario(ID, datos_usuario):
    update_usuario_sql = f"""
                UPDATE datosusuario 
                SET edad='{datos_usuario['edad']}', año='{datos_usuario['año']}', peso='{datos_usuario['peso']}',  altura='{datos_usuario['altura']}', infogen='{datos_usuario['infogen']}'
                WHERE ID='{ID}' 
                """
    db = basedatos()
    db.ejecutar_sql(update_usuario_sql)
