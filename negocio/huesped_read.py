from modelos.huesped import Huesped
from prettytable import PrettyTable
from datos import obtener_datos_objetos

def listar_huespedes():
    tabla_huespedes = PrettyTable()
    tabla_huespedes.field_names = ['ID', 'Nombre', 'Apellido', 'Teléfono', 'Email']
    
    listado_huespedes = obtener_datos_objetos(Huesped)
    if listado_huespedes:
        for huesped in listado_huespedes:
            tabla_huespedes.add_row([huesped.id, huesped.nombre, huesped.apellido, huesped.telefono, huesped.email])
        print(tabla_huespedes)
    else:
        print("No hay huéspedes registrados.")
