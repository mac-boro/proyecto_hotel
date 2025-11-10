from datos.conexion import sesion
from modelos.huesped import Huesped
from auxiliares.normalizar_cadena import normalizar_cadena

def obtener_objeto_hab(objeto):
    try:
        listado_objetos = sesion.query(objeto).filter_by(habilitado=True).all()
        if len(listado_objetos) > 0:
            return listado_objetos
    except Exception as e:
        print(f"Error: {e}")

def obtener_objeto_deshab(objeto):
    try:
        listado_objetos = sesion.query(objeto).filter_by(habilitado=False).all()
        if len(listado_objetos) > 0:
            return listado_objetos
    except Exception as e:
        print(f"Error: {e}")

def obtener_huesped_nombre(nombre_huesped):
    listado_huesped = obtener_objeto_hab(Huesped)
    huesped_encontrado = None
    if listado_huesped:
        for nombre in listado_huesped:
            if normalizar_cadena(nombre.nombre_huesped) == normalizar_cadena(nombre_huesped):
                huesped_encontrado = nombre
                break
    return huesped_encontrado