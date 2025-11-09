def obtener_float_valido(mensaje):
    """Pide y valida una entrada para que sea un número flotante positivo."""
    precio_valido = None
    while precio_valido is None:
        try:
            precio = float(input(mensaje))
            if precio >= 0:
                precio_valido = precio
            else:
                print("❗ El valor debe ser positivo.")
        except ValueError:
            print("❗ Entrada inválida. Por favor, ingrese un número (ej: 150.50).")
    return precio_valido