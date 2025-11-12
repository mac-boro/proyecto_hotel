from negocio.habitacion_read import lista_habitaciones
from negocio.huesped_create import insertar_huesped
from negocio.habitación_update import crear_reserva
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
        print("1.  Crear Nueva Reserva (incl. Servicios/Desc.)")
        print("2.  Extender Reserva")
        print("3.  Listar Reservas")
        print("4.  Liberar Habitación")
        print("---------")
        print("Huéspedes")
        print("---------")
        print("5.  Registrar Nuevo Huésped")
        print("6.  Actualizar Huésped")
        print("----------------")
        print("Facturas y Pagos")
        print("----------------")
        print("7.  Facturación")
        print("8.  Registro de Pago")
        print("----------------------")
        print("Servicios y Descuentos")
        print("----------------------")
        print("9.  Agregar Servicio")
        print("10. Actualizar Servicio")
        print("11. Agregar Descuento")
        print("12. Actualizar Descuento")
        print("======================================")        
        print("13. Salir")
        print("======================================")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            crear_reserva()
            print("Opción no disponbile temporalmente. 😵")
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
            #modificar_huesped()
            print("Opción no disponbile temporalmente. 😵")
        elif opcion == '7':
            #crear_factura()
            print("Opción no disponbile temporalmente. 😵")
        elif opcion == '8':
            #listar_reserva
            print("Opción no disponbile temporalmente. 😵")
        elif opcion == '9':
            #listar_reservas(
            print("Opción no disponbile temporalmente. 😵")
        elif opcion == '10':
            #listar_reservas(
            print("Opción no disponbile temporalmente. 😵")
        elif opcion == '11':
            #listar_reservas(
            print("Opción no disponbile temporalmente. 😵")
        elif opcion == '12':
            #listar_reservas(
            print("Opción no disponbile temporalmente. 😵")
        elif opcion == '13':
            print("Saliendo del sistema. ¡Hasta pronto!")
            ejecutando = False 
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar la aplicación
if __name__ == "__main__":
    menu_principal()