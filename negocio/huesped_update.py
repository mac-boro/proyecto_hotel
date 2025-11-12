from ui.iu_huesped import ingresar_nombre_huesped, ingresar_apellido_huesped, ingresar_nuevo_nombre_huesped, ingresar_nuevo_apellido_huesped, ingresar_nuevo_telefono_huesped, ingresar_nuevo_email_huesped
from datos.obtener_datos import obtener_huesped_nombre
from datos.modificar_datos import modificar_objeto

def modificar_huesped():
    nombre = ingresar_nombre_huesped()
    apellido =  ingresar_apellido_huesped()

    huesped_encontrado = obtener_huesped_nombre(nombre)
    if huesped_encontrado:
        nuevo_nombre_huesped = ingresar_nuevo_nombre_huesped()
        nuevo_apellido_huesped = ingresar_nuevo_apellido_huesped()
        nuevo_telefono_huesped = ingresar_nuevo_telefono_huesped
        nuevo_email_huesped = ingresar_nuevo_email_huesped
        if nuevo_nombre_huesped != '':
            huesped_encontrado.nombre = nuevo_nombre_huesped.title()
        if nuevo_apellido_huesped != '':
            huesped_encontrado.apellido = nuevo_apellido_huesped.title()
        if nuevo_nombre_huesped != '':
            huesped_encontrado.telefono = nuevo_telefono_huesped
        if nuevo_email_huesped != '':
            huesped_encontrado.email = nuevo_email_huesped
        modificar_objeto()