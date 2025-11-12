from ui.iu_servicio import ingresar_nombre_servicio, ingresar_nuevo_nombre_servicio, ingresar_nuevo_precio_servicio
from datos.obtener_datos import obtener_servicio_nombre
from datos.modificar_datos import modificar_objeto

def modificar_servicio():
    nombre = ingresar_nombre_servicio()

    servicio_encontrado = obtener_servicio_nombre(nombre)
    if servicio_encontrado:
        nuevo_nombre_servicio = ingresar_nuevo_nombre_servicio()
        nuevo_precio_servicio = ingresar_nuevo_precio_servicio()
        if nuevo_nombre_servicio != '':
            servicio_encontrado.nombre = nuevo_nombre_servicio.title()
        if nuevo_precio_servicio != '':
            servicio_encontrado.precio = nuevo_precio_servicio
        modificar_objeto()