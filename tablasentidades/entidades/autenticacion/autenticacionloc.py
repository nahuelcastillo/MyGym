from tablasentidades.entidades.locales import localesgym as modelo_local


def obtener_locales():
    return modelo_local.obtener_locales()

def obtener_loal(nombreLocal):
    local = modelo_local.obtener_local(nombreLocal)
    if len(local) == 0:
        raise Exception("el local no existe")
    return local[0]


