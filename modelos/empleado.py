class Empleado:
    def __init__(self, id_empleado, nombre, puesto, salario):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def __str__(self):
        return f"Empleado: {self.nombre} - Puesto: {self.puesto} - Salario: ${self.salario}"
