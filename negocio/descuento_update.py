from ui.iu_descuento import ingresar_nombre_descuento, ingresar_nuevo_nombre_descuento, ingresar_nuevo_porcentaje_descuento
from datos.obtener_datos import obtener_descuento_nombre
from datos.modificar_datos import modificar_objeto

def modificar_descuento():
    nombre = ingresar_nombre_descuento()

    descuento_encontrado = obtener_descuento_nombre(nombre)
    if descuento_encontrado:
        nuevo_nombre_descuento = ingresar_nuevo_nombre_descuento()
        nuevo_porcentaje_descuento = ingresar_nuevo_porcentaje_descuento()
        if nuevo_nombre_descuento != '':
            descuento_encontrado.nombre = nuevo_nombre_descuento.title()
        if nuevo_porcentaje_descuento != '':
            descuento_encontrado.porcentaje = nuevo_porcentaje_descuento
        modificar_objeto()