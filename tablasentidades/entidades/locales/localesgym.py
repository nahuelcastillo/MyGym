from tablasentidades.tablas.conexionbd import basedatos


def crear_local(nombreLocal, direccion, telefono, correoelectronico, instagram, info, idusuario):
    crear_local_sql = f"""
            INSERT INTO LocalClubGym(nombreLocal, direccion, telefono, correoelectronico, instagram, info, idusuario)
            VALUES ('{nombreLocal}', '{direccion}', '{telefono}', '{correoelectronico}', '{instagram}', '{info}', '{idusuario}')
    """
    bd = basedatos()
    bd.ejecutar_sql(crear_local_sql)

def eliminar_local(idusuario):
    eliminar_local_sql = f"""
            DELETE FROM LocalClubGym WHERE idusuario = '{idusuario}'
    """
    db = basedatos()
    db.ejecutar_sql(eliminar_local_sql)


def update_local(idlocal, datos_local):
    update_local_sql = f"""
            UPDATE LocalClubGym 
            SET nombreLocal='{datos_local['nombreLocal']}', direccion='{datos_local['direccion']}', telefono='{datos_local['telefono']}', correoelectronico='{datos_local['correoelectronico']}', instagram='{datos_local['instagram']}, info='{datos_local['info']}' 
            WHERE idlocal='{idlocal}' 
            """
    db = basedatos()
    db.ejecutar_sql(update_local_sql)


def obtener_locales():
    obtener_locales_sql = f"""
        SELECT idlocal, nombreLocal, direccion, telefono, correoelectronico, instagram, info
        FROM LocalClubGym 
    """
    bd = basedatos()
    return [{"idlocal": registro[0],
             "nombreLocal": registro[1],
             "direccion": registro[2],
             "telefono": registro[3],
             "correoelectronico": registro[4],
             "instagram": registro[5],
             "info": registro[6]
             } for registro in bd.ejecutar_sql(obtener_locales_sql)]


def obtener_local(nombreLocal):
    obtener_local_sql = f"""
        SELECT  *
        FROM LocalClubGym  
        WHERE nombreLocal = '{nombreLocal}'
    """
    bd = basedatos()
    return [{"idlocal": registro[0],
             "nombreLocal": registro[1],
             "direccion": registro[2],
             "telefono": registro[3],
             "correoelectronico": registro[4],
             "instagram": registro[5],
             "info": registro[6]
             } for registro in bd.ejecutar_sql(obtener_local_sql)]
