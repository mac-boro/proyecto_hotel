from negocio.habitacion_read import lista_habitaciones
from negocio.huesped_create import insertar_huesped_reserva
from ui.iu_habitacion import ingresar_habitacion_reserva
from ui.iu_servicio import solicitar_servicio

def crear_reserva():
    print(lista_habitaciones())
    reserva = ingresar_habitacion_reserva()
    huesped = insertar_huesped_reserva()
    servicio = solicitar_servicio()
    descuento = 1

    print('{}{}{}{}'.format(reserva, huesped, servicio, descuento))