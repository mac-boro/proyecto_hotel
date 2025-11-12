from negocio.reserva_create import crear_reserva
from negocio.habitacion_read import lista_habitaciones
from negocio.huesped_create import insertar_huesped
from negocio.huesped_update import modificar_huesped
from negocio.servicio_create import insertar_servicio
from negocio.servicio_update import modificar_servicio
from negocio.descuento_create import insertar_descuento
from negocio.descuento_update import modificar_descuento
from datos.conexion import sesion
from auxiliares.info_aplicacion import nombre_aplicacion
from auxiliares.version import numero_version

def menu_principal():
    ejecutando = True 
    while ejecutando:
        print("\n======================================")
        print("{} v{}".format(nombre_aplicacion, numero_version))
        print("======================================")
        print("--------")
        print("Reservas")
        print("--------")
        print("[1]  Crear Nueva Reserva (incl. Servicios/Desc.)")
        print("[2]  Extender Reserva")
        print("[3]  Listar Reservas")
        print("[4]  Liberar Habitación")
        print("---------")
        print("Huéspedes")
        print("---------")
        print("[5]  Registrar Nuevo Huésped")
        print("[6]  Actualizar Huésped")
        print("----------------")
        print("Facturas y Pagos")
        print("----------------")
        print("[7]  Facturación")
        print("[8]  Registro de Pago")
        print("----------------------")
        print("Servicios y Descuentos")
        print("----------------------")
        print("[9]  Agregar Servicio")
        print("[10] Actualizar Servicio")
        print("[11] Agregar Descuento")
        print("[12] Actualizar Descuento")
        print("======================================")        
        print("[13] Salir")
        print("======================================")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            crear_reserva()
        elif opcion == '2':
            #extender_reservas()
            print("Opción no disponbile temporalmente. 😵")
        elif opcion == '3':
            lista_habitaciones()
        elif opcion == '4':
            #facturar_reserva()
            print("Opción no disponbile temporalmente. 😵")
        elif opcion == '5':
            insertar_huesped()
        elif opcion == '6':
            modificar_huesped()
        elif opcion == '7':
            #insertar_factura()
            print("Opción no disponbile temporalmente. 😵")
        elif opcion == '8':
            #insertar_pago()
            print("Opción no disponbile temporalmente. 😵")
        elif opcion == '9':
            insertar_servicio()
        elif opcion == '10':
            modificar_servicio()
        elif opcion == '11':
            insertar_descuento()
        elif opcion == '12':
            modificar_descuento()
        elif opcion == '13':
            print("Saliendo del sistema. ¡Hasta pronto!")
            ejecutando = False 
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar la aplicación
if __name__ == "__main__":
    menu_principal()