from modelos.descuento import Descuento
from prettytable import PrettyTable
from datos.obtener_datos import obtener_objeto_hab

def listar_descuentos():
    tabla_descuento = PrettyTable()
    tabla_descuento.field_names = ['ID', 'Nombre', '%']
    
    listado_descuento = obtener_objeto_hab(Descuento)
    if listado_descuento:
        for descuento in listado_descuento:
            tabla_descuento.add_row([descuento.id, descuento.nombre, descuento.porcentaje])
        print(tabla_descuento)
    else:
        print("No hay descuentos registrados.")