from auxiliares.validar_entero import obtener_entero_valido

def ingresar_nombre_huesped():
    nombre = input('📋 Ingrese el nombre del huesped: ')
    return(nombre)

def ingresar_apellido_huesped():
    apellido = input('📋 Ingrese el apellido del huesped: ')
    return(apellido)

def ingresar_telefono_huesped():
    telefono = obtener_entero_valido('📞 Ingrese el número telefonico del huesped: ')
    return(telefono)

def ingresar_email_huesped():
    email = input('📧 Ingrese el correo electronico del huesped: ')
    return(email)

def ingresar_nuevo_nombre_huesped():
    nombre = input('📋 Ingrese el nuevo nombre del huesped: ')
    return(nombre)

def ingresar_nuevo_apellido_huesped():
    apellido = input('📋 Ingrese el nuevo apellido del huesped: ')
    return(apellido)

def ingresar_nuevo_telefono_huesped():
    telefono = obtener_entero_valido('📞 Ingrese el nuevo número telefonico del huesped: ')
    return(telefono)

def ingresar_nuevo_email_huesped():
    email = input('📧 Ingrese el nuevo correo electronico del huesped: ')
    return(email)