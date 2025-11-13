from datos.obtener_datos import obtener_habitacion_id
from datos.modificar_datos import modificar_objeto

def modificar_habitacion_hab(id):
    
    habitacion_encontrado = obtener_habitacion_id(id)
    if habitacion_encontrado:
        id_habitacion = id
        if id_habitacion != '':
            habitacion_encontrado.id = id_habitacion
        modificar_objeto()