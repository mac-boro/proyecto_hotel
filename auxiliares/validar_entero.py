def obtener_entero_valido(mensaje):
    """Pide y valida una entrada para que sea un número entero positivo."""
    valor_valido = None
    while valor_valido is None:
        valor_str = input(mensaje)
        if valor_str.isdigit():
            valor_valido = valor_str
        else:
            print("❗ Entrada inválida. Por favor, ingrese solo números (dígitos).")
    return valor_valido