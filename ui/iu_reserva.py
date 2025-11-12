import datetime
from auxiliares.validar_entero import obtener_entero_valido

def ingresar_fecha_entrada():
    año = int(obtener_entero_valido('Ingrese el año de la fecha de entrada: '))
    mes = int(obtener_entero_valido('Ingrese el mes de la fecha de entrada: '))
    dia = int(obtener_entero_valido('Ingrese el día de la fecha de entrada: '))
    
    fecha_entrada = datetime.datetime(año, mes, dia)
    return(fecha_entrada)

def ingresar_fecha_salida():
    año = int(obtener_entero_valido('Ingrese el año de la fecha de salida: '))
    mes = int(obtener_entero_valido('Ingrese el mes de la fecha de salida: '))
    dia = int(obtener_entero_valido('Ingrese el día de la fecha de salida: '))

    fecha_salida = datetime.datetime(año, mes, dia)
    return(fecha_salida)