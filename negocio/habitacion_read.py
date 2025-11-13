from modelos.habitacion import Habitacion
from prettytable import PrettyTable
from datos.obtener_datos import obtener_objeto_hab 


def lista_habitaciones():
    tabla_habitaciones = PrettyTable()
    tabla_habitaciones.field_names = ['ID', 'N°', 'Tipo', 'Precio']
    lista_habitaciones = obtener_objeto_hab(Habitacion)
    if lista_habitaciones:
        for habitacion in lista_habitaciones:
            tabla_habitaciones.add_row(
                [habitacion.id, habitacion.numero, habitacion.tipo, habitacion.precio])
        print(tabla_habitaciones)
