from datos.insertar_datos import insertar_objeto
from datos.obtener_datos import obtener_huesped_nombre
from modelos.huesped import Huesped

def insertar_huesped():
    nombre = input('Ingrese el nombre del huesped: ')
    apellido = input('Ingrese el apellido del huesped: ')
    telefono = int(input('Ingrese el número telefonico del huesped: '))
    email = input('Ingrese el correo electronico del huesped: ')

    respuesta = obtener_huesped_nombre(nombre)
    if respuesta == None:
        # INSTANCIA DE CLASE
        nuevo_huesped = Husped(nombre=nombre.title(), apellido=apellido.title(), telefono=telefono.title(), email=email.title())
        insertar_objeto(nuevo_huesped)
    else:
        print('Su huesped YA existe en base de datos.')