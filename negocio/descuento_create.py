from modelos.descuento import Descuento
from datos.obtener_datos import obtener_descuento_nombre
from datos.insertar_datos import insertar_objeto
from ui.iu_descuento import ingresar_nombre_descuento, ingresar_porcentaje_descuento

def insertar_descuento():
    nombre = ingresar_nombre_descuento()

    respuesta = obtener_descuento_nombre(nombre)
    if respuesta == None:
        porcentaje = ingresar_porcentaje_descuento()
        nuevo_descuento = Descuento(nombre=nombre.title(), porcentaje=porcentaje)
        insertar_objeto(nuevo_descuento)
    else:
        print('Su descuento YA existe en base de datos.')