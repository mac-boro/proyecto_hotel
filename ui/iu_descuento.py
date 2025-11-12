from auxiliares.validar_entero import obtener_entero_valido
from negocio.descuento_read import listar_descuentos

def ingresar_nombre_descuento():
    nombre = input('Ingrese el nombre del descuento: ')
    return(nombre)

def ingresar_porcentaje_descuento():
    porcentaje = int(obtener_entero_valido('Ingrese el porcentaje del descuento (con numeros enteros): %'))
    return(porcentaje)

def ingresar_nuevo_nombre_descuento():
    nombre = input('Ingrese el nuevo nombre del descuento: ')
    return(nombre)

def ingresar_nuevo_porcentaje_descuento():
    porcentaje = int(obtener_entero_valido('Ingrese el nuevo porcentaje del descuento: $'))
    return(porcentaje)

def solicitar_descuento():
    print('¿Desea agregar descuento a su reserva?')
    print('[1] Si')
    print('[2] No')

    opcion = input('\nSeleccione una opción [1 o 2]: ')
    opcion_valida = False
    while opcion == False:
        if opcion == '1':
            print(listar_descuentos())
            id = int(input(obtener_entero_valido('Ingrese el ID del descuento solicitado: ')))
            return(id)
        elif opcion == '2':
            id = 1
            return(id)
        else:
            print('Ingrese una opción valida [1 o 2]')