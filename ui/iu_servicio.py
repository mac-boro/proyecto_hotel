from negocio.servicio_read import listar_servicios
from auxiliares.validar_entero import obtener_entero_valido
from auxiliares.validar_float import obtener_float_valido
from datos.conexion import sesion
from modelos.servicio import Servicio

def ingresar_nombre_servicio():
    nombre = input('Ingrese el nombre del servicio: ')
    return(nombre)

def ingresar_precio_servicio():
    precio = float(obtener_float_valido('Ingrese el precio del servicio: $'))
    return(precio)

def ingresar_nuevo_nombre_servicio():
    nombre = input('Ingrese el nuevo nombre del servicio: ')
    return(nombre)

def ingresar_nuevo_precio_servicio():
    precio = float(obtener_float_valido('Ingrese el nuevo precio del servicio: $'))
    return(precio)

def solicitar_servicio():
    print('¿Desea agregar servicios a su reserva?')
    print('[1] Si')
    print('[2] No')

    opcion = input('\nSeleccione una opción [1 o 2]: ')
    opcion_valida = False
    while opcion == False:
        if opcion == '1':
            print(listar_servicios())
            id = int(input(obtener_entero_valido('Ingrese el ID del servicio solicitado: ')))
            return(id)
        elif opcion == '2':
            id = 1
            return(id)
        else:
            print('Ingrese una opción valida [1 o 2]')