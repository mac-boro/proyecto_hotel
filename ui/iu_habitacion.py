from auxiliares.validar_entero import obtener_entero_valido

def ingresar_habitacion_reserva():
  id = obtener_entero_valido('Ingrese el id de la habitacion a reservar: ')
  return(id)