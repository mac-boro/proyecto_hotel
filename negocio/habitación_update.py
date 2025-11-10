from negocio.habitacion_read import lista_habitaciones
from ui.iu_habitacion import ingresar_habitacion_reserva

def crear_reserva():
    print(lista_habitaciones())
    reserva = ingresar_habitacion_reserva()
    