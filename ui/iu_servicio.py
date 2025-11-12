from negocio.servicios_read import listar_servicios
from auxiliares.validar_entero import obtener_entero_valido
from datos.conexion import sesion
from modelos.servicio import Servicio

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
            return(sesion.query(Servicio).filter_by(id=id).all())
        elif opcion == '2':
            return(sesion.query(Servicio).filter_by(id=1).all())
        else:
            print('Ingrese una opción valida [1 o 2]')