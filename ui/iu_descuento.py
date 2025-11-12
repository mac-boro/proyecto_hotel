from auxiliares.validar_entero import obtener_entero_valido

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