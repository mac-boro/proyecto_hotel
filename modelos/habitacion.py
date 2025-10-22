class Habitacion:
    def __init__(self, numero, tipo, precio_noche, esta_disponible=True):
        self.numero = numero
        self.tipo = tipo  # Puede ser "Individual", "Doble", "Suite", etc.
        self.precio_noche = precio_noche
        self.esta_disponible = esta_disponible
    
    def reservar(self):
        """Marcar la habitación como reservada."""
        self.esta_disponible = False

    def liberar(self):
        """Marcar la habitación como disponible."""
        self.esta_disponible = True

    def __str__(self):
        return f"Habitación {self.numero} - Tipo: {self.tipo} - ${self.precio_noche}/noche"
