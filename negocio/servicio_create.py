from modelos.servicio import Servicio
from datos.obtener_datos import obtener_servicio_nombre
from datos.insertar_datos import insertar_objeto
from ui.iu_servicio import ingresar_nombre_servicio, ingresar_precio_servicio

def insertar_servicio():
    nombre = ingresar_nombre_servicio()

    respuesta = obtener_servicio_nombre(nombre)
    if respuesta == None:
        precio = ingresar_precio_servicio()
        nuevo_servicio = Servicio(nombre=nombre.title(), precio=precio)
        insertar_objeto(nuevo_servicio)
    else:
        print('Su servicio YA existe en base de datos.')