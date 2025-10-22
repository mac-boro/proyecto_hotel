class Reserva:
    def __init__(self, id_reserva, cliente, habitacion, fecha_inicio, fecha_fin):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = "Confirmada"  # Puede ser "Confirmada", "Cancelada", "Finalizada"
    
    def cancelar(self):
        """Cancelar la reserva."""
        self.estado = "Cancelada"
        self.habitacion.liberar()

    def finalizar(self):
        """Finalizar la reserva y liberar la habitación."""
        self.estado = "Finalizada"
        self.habitacion.liberar()

    def __str__(self):
        return f"Reserva {self.id_reserva} - Cliente: {self.cliente.nombre} - Habitación: {self.habitacion.numero} - Estado: {self.estado}"
