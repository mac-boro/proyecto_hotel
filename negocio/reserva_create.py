from modelos.reserva import Reserva
from datos.insertar_datos import insertar_objeto
from negocio.habitacion_read import lista_habitaciones
from negocio.habitacion_update import modificar_habitacion_hab
from negocio.huesped_create import insertar_huesped_reserva
from ui.iu_habitacion import ingresar_habitacion_reserva
from ui.iu_servicio import solicitar_servicio
from ui.iu_descuento import solicitar_descuento
from ui.iu_reserva import ingresar_fecha_entrada, ingresar_fecha_salida

def crear_reserva():
    print(lista_habitaciones())
    habitacion = ingresar_habitacion_reserva()
    huesped = insertar_huesped_reserva()
    servicio = solicitar_servicio()
    descuento = solicitar_descuento()
    fecha_entrada = ingresar_fecha_entrada()
    fecha_salida = ingresar_fecha_salida()
    total = 100
    habilitado = True

    nueva_reserva = Reserva(id_huesped=huesped, id_habitacion=habitacion, id_descuento=descuento, id_servicio=servicio, fecha_entrada=fecha_entrada, fecha_salida=fecha_salida, total=total, habilitado=habilitado)
    insertar_objeto(nueva_reserva)
    modificar_habitacion_hab(habitacion)

    print('¡Reserva creada exitosamente!')