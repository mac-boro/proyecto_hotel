from modelos.huesped import Huesped
from prettytable import PrettyTable
from datos.obtener_datos import obtener_objeto_hab

def listar_huespedes():
    tabla_huespedes = PrettyTable()
    tabla_huespedes.field_names = ['ID', 'Nombre', 'Apellido', 'Teléfono', 'Email']
    
    listado_huespedes = obtener_objeto_hab(Huesped)
    if listado_huespedes:
        for huesped in listado_huespedes:
            tabla_huespedes.add_row([huesped.id, huesped.nombre, huesped.apellido, huesped.telefono, huesped.email])
        print(tabla_huespedes)
    else:
        print("No hay huéspedes registrados.")