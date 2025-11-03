from datos.conexion import sesion

def obtener_objeto():
    try:
        listado_objetos = sesion.query(objeto).all()
        if len(listado_objetos) > 0:
            return listado_objetos
    except Exception as e:
        print(f"Error: {e}")