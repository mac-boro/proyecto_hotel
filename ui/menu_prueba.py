from negocio.habitacion_read import lista_habitaciones
from negocio.huesped_create import insertar_huesped
from datos.conexion import sesion
from auxiliares.info_aplicacion import nombre_aplicacion
from auxiliares.version import numero_version

def menu_prueba():
    ejecutando = True 
    while ejecutando:
        print("\n======================================")
        print("{} v{}".format(nombre_aplicacion, numero_version))
        print("======================================")
        print("1. Crear Nueva Reserva (incl. Servicios/Desc.)")
        print("2. Listar Reservas")
        print("3. Registrar Nuevo Huésped")
        print("4. Facturación y Registro de Pago")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            #crear_reserva()
            print("")
        elif opcion == '2':
            #listar_reservas()
            lista_habitaciones()
        elif opcion == '3':
            insertar_huesped()
        elif opcion == '4':
            #facturar_reserva()
            print("")
        elif opcion == '5':
            print("Saliendo del sistema. ¡Hasta pronto!")
            ejecutando = False 
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar la aplicación
if __name__ == "__main__":
    menu_prueba()