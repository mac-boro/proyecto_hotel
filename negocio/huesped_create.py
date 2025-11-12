from datos.insertar_datos import insertar_objeto
from datos.obtener_datos import obtener_huesped_nombre
from datos.conexion import sesion
from ui.iu_huesped import ingresar_nombre_huesped, ingresar_apellido_huesped, ingresar_telefono_huesped, ingresar_email_huesped
from modelos.huesped import Huesped

def insertar_huesped():
    nombre = ingresar_nombre_huesped()
    apellido = ingresar_apellido_huesped()

    respuesta = obtener_huesped_nombre(nombre)
    if respuesta == None:
        telefono = ingresar_telefono_huesped()
        email = ingresar_email_huesped()
        # INSTANCIA DE CLASE
        nuevo_huesped = Huesped(nombre=nombre.title(), apellido=apellido.title(), telefono=telefono, email=email)
        insertar_objeto(nuevo_huesped)
    else:
        print('Su huesped YA existe en base de datos.')

def insertar_huesped_reserva():
    nombre = ingresar_nombre_huesped()
    apellido = ingresar_apellido_huesped()

    respuesta = obtener_huesped_nombre(nombre)
    if respuesta == None:
        telefono = ingresar_telefono_huesped()
        email = ingresar_email_huesped()
        # INSTANCIA DE CLASE
        nuevo_huesped = Huesped(nombre=nombre.title(), apellido=apellido.title(), telefono=telefono, email=email)
        insertar_objeto(nuevo_huesped)
        return(nuevo_huesped)
    else:
        print(respuesta)
        return(sesion.query(Huesped).filter_by(nombre=respuesta).all())