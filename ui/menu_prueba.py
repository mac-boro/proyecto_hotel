from negocio.huesped_create import insertar_huesped
from datos.conexion import sesion

def menu_prueba():
    """Presenta el menú de opciones al usuario, usando un flag booleano en lugar de break."""
    ejecutando = True 
    while ejecutando:
        print("\n==================================")
        print("  SISTEMA DE GESTIÓN HOTELERA (v1.0)")
        print("==================================")
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
            print("")
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