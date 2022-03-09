from tablasentidades.tablas.conexionbd import basedatos


def crear_reseña(ID_USUARIO, reseña, ID_LOCAL):
    crear_reseña_sql = f"""
            INSERT INTO reseñas(ID_USUARIO, reseña, ID_LOCAL)
            VALUES ('{ID_USUARIO}', '{reseña}', '{ID_LOCAL}')
    """
    bd = basedatos()
    bd.ejecutar_sql(crear_reseña_sql)


def obtener_reseña_local(ID_LOCAL):
    obtener_reseña_local_sql = f"""
        SELECT  *
        FROM reseñas  
        WHERE ID_LOCAL = '{ID_LOCAL}'
    """
    bd = basedatos()
    return [{"IDreseña": registro[0],
             "ID_USUARIO": registro[1],
             "reseña": registro[2],
             "ID_LOCAL": registro[3]}
            for registro in bd.ejecutar_sql(obtener_reseña_local_sql)]
