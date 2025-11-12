from modelos.servicio import Servicio
from prettytable import PrettyTable
from datos.obtener_datos import obtener_objeto_hab

def listar_servicios():
    tabla_servicios = PrettyTable()
    tabla_servicios.field_names = ['ID', 'Nombre', 'Precio']
    
    listado_servicios = obtener_objeto_hab(Servicio)
    if listado_servicios:
        for servicio in listado_servicios:
            tabla_servicios.add_row([servicio.id, servicio.nombre, servicio.precio])
        print(tabla_servicios)
    else:
        print("No hay servicios registrados.")