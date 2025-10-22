class Pago:
    def __init__(self, id_pago, cliente, monto, metodo_pago, fecha_pago):
        self.id_pago = id_pago
        self.cliente = cliente
        self.monto = monto
        self.metodo_pago = metodo_pago  # Ej: "Tarjeta de crédito", "Efectivo"
        self.fecha_pago = fecha_pago

    def __str__(self):
        return f"Pago {self.id_pago} - Cliente: {self.cliente.nombre} - Monto: ${self.monto} - Método de pago: {self.metodo_pago}"
