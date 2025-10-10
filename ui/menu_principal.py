import time


# --- SIMULACIÓN DE LA BASE DE DATOS  ---

HUESPEDES = {}
RESERVAS = {}
FACTURAS = {}
# Tablas para Servicios y Descuentos
SERVICIOS_DISPONIBLES = {
    'S001': {'nombre': 'Desayuno Buffet', 'precio': 15.00},
    'S002': {'nombre': 'Parking/Estacionamiento', 'precio': 10.00},
    'S003': {'nombre': 'Lavandería Rápida', 'precio': 25.00}
}
DESCUENTOS_DISPONIBLES = {
    'D001': {'nombre': 'Promoción Fin de Semana', 'porcentaje': 0.10}, # 10%
    'D002': {'nombre': 'Estadía Larga', 'porcentaje': 0.15},          # 15%
    'D003': {'nombre': 'Tercera Edad', 'porcentaje': 0.05}             # 5%
}

# Contadores globales (simulan AUTO_INCREMENT)
ID_HUESPED_CONTADOR = 0
ID_RESERVA_CONTADOR = 0
ID_FACTURA_CONTADOR = 0

def generar_id(prefijo):
    """Genera un ID simple y globalmente único para la simulación."""
    global ID_HUESPED_CONTADOR, ID_RESERVA_CONTADOR, ID_FACTURA_CONTADOR
    
    if prefijo == 'H':
        ID_HUESPED_CONTADOR += 1
        return f"H{ID_HUESPED_CONTADOR:04d}"
    elif prefijo == 'R':
        ID_RESERVA_CONTADOR += 1
        return f"R{ID_RESERVA_CONTADOR:04d}"
    elif prefijo == 'F':
        ID_FACTURA_CONTADOR += 1
        return f"F{ID_FACTURA_CONTADOR:04d}"
    return "" # Retorno seguro

# ----------------------------------------------------
# --- FUNCIONES AUXILIARES DE VALIDACIÓN  ---
# ----------------------------------------------------

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

# ------------------------------------
# --- MÓDULOS DE LÓGICA DEL SISTEMA ---
# ------------------------------------

def crear_huesped():
    """Función para registrar un nuevo huésped, usando la validación de teléfono."""
    print("\n--- REGISTRAR NUEVO HUÉSPED ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    
    # Validación: El teléfono debe ser solo dígitos (usa obtener_entero_valido)
    telefono = obtener_entero_valido("Teléfono (solo dígitos): ")
    
    huesped_id = generar_id('H')
    HUESPEDES[huesped_id] = {
        'nombre': nombre,
        'apellido': apellido,
        'email': email,
        'telefono': telefono
    }
    print(f"\n✅ Huésped {nombre} {apellido} registrado con ID: {huesped_id}")
    return huesped_id

def listar_reservas():
    """Muestra todas las reservas registradas."""
    print("\n--- LISTADO DE RESERVAS ---")
    if not RESERVAS:
        print("No hay reservas registradas.")
        return # Sale de la función

    print(f"{'ID':<6} | {'Huésped':<20} | {'Hab.':<5} | {'Entrada':<10} | {'Total':<8} | {'Estado':<10}")
    print("-" * 65)
    
    for res_id, res in RESERVAS.items():
        huesped = HUESPEDES.get(res.get('id_huesped'))
        
        nombre_completo = (
            f"{huesped.get('nombre', 'N/A')} {huesped.get('apellido', '')}"
            if huesped else "Huésped NO ENCONTRADO"
        )
            
        try:
            print(
                f"{res_id:<6} | "
                f"{nombre_completo[:20]:<20} | "
                f"{res.get('habitacion', 'N/A'):<5} | "
                f"{res.get('fecha_entrada', 'N/A'):<10} | "
                f"${res.get('total_final', 0.0):<7.2f} | "
                f"{res.get('estado', 'N/A'):<10}"
            )
        except Exception as e:
            print(f"❌ Error al mostrar la reserva {res_id}: {e}")


def crear_reserva():
    """Función para crear una nueva reserva, incluyendo servicios y descuentos."""
    print("\n--- CREAR NUEVA RESERVA ---")
    
    # ---  Huésped ---
    huesped_id = None
    email_busqueda = input("Email del Huésped (deje vacío para crear uno nuevo): ")
    
    if email_busqueda:
        for hid, h in HUESPEDES.items():
            if h.get('email', '').lower() == email_busqueda.lower():
                huesped_id = hid
                print(f"Huésped encontrado: {h['nombre']} {h['apellido']}")
                return 
                      
        
    if not huesped_id:
        print("Huésped no encontrado o no se proporcionó email. Creando nuevo huésped...")
        huesped_id = crear_huesped()

    # ---  Alojamiento y Precio Base ---
    fecha_entrada = input("Fecha de Entrada (YYYY-MM-DD): ")
    fecha_salida = input("Fecha de Salida (YYYY-MM-DD): ")
    
    # Validación: La habitación debe ser solo dígitos 
    habitacion = obtener_entero_valido("Número de Habitación (solo dígitos): ")
    
    # Validación: El precio base debe ser un flotante 
    precio_base = obtener_float_valido("Precio base de la estadía: $")
            
    # ---  Servicios Adicionales  ---
    costo_servicios = 0.0
    servicios_seleccionados = []
    print("\n--- AGREGAR SERVICIOS ---")
    
    continuar_servicios = True
    while continuar_servicios:
        print("\nServicios disponibles:")
        print(f"{'ID':<5} | {'Nombre':<25} | {'Precio':<8}")
        print("-" * 40)
        for sid, s in SERVICIOS_DISPONIBLES.items():
            print(f"{sid:<5} | {s['nombre']:<25} | ${s['precio']:<7.2f}")

        servicio_id = input("Ingrese ID de servicio a agregar (o 'n' para continuar): ").upper()
        
        if servicio_id == 'N':
            continuar_servicios = False 
        elif servicio_id in SERVICIOS_DISPONIBLES:
            serv = SERVICIOS_DISPONIBLES[servicio_id]
            costo_servicios += serv['precio']
            servicios_seleccionados.append(serv['nombre'])
            print(f"✅ Agregado: {serv['nombre']}. Costo total de servicios: ${costo_servicios:.2f}")
        else:
            print("ID de servicio no válido.")

    # ---  Descuento (Relación 0..1:1) ---
    descuento_aplicado = 0.0
    descuento_nombre = "Ninguno"
    descuento_porcentaje = 0.0
    
    print("\n--- APLICAR DESCUENTO ---")
    print(f"{'ID':<5} | {'Nombre':<25} | {'Porcentaje':<10}")
    print("-" * 45)
    for did, d in DESCUENTOS_DISPONIBLES.items():
        print(f"{did:<5} | {d['nombre']:<25} | {d['porcentaje']*100:<10.0f}%")

    desc_id = input("Ingrese ID de descuento a aplicar (o 'n' para omitir): ").upper()
    
    if desc_id in DESCUENTOS_DISPONIBLES:
        desc = DESCUENTOS_DISPONIBLES[desc_id]
        descuento_porcentaje = desc['porcentaje']
        descuento_nombre = desc['nombre']
        
        subtotal = precio_base + costo_servicios
        descuento_aplicado = subtotal * descuento_porcentaje
        print(f"✅ Descuento aplicado: {descuento_nombre} ({descuento_porcentaje*100:.0f}%).")

    # --- Cálculo Total ---
    total_neto = precio_base + costo_servicios
    total_final = total_neto - descuento_aplicado
    
    print("\n--- RESUMEN DE RESERVA ---")
    print(f"Precio Base Alojamiento: ${precio_base:.2f}")
    print(f"Costo Servicios:         ${costo_servicios:.2f}")
    print(f"Subtotal:                ${total_neto:.2f}")
    print(f"Descuento ({descuento_nombre}): -${descuento_aplicado:.2f}")
    print(f"TOTAL FINAL:             ${total_final:.2f}")
    
    # --- Creación de la Reserva ---
    reserva_id = generar_id('R')
    RESERVAS[reserva_id] = {
        'id_huesped': huesped_id,
        'habitacion': habitacion,
        'fecha_entrada': fecha_entrada,
        'fecha_salida': fecha_salida,
        'precio_base': precio_base,
        'servicios': servicios_seleccionados,
        'costo_servicios': costo_servicios,
        'descuento_aplicado': descuento_aplicado,
        'total_final': total_final,
        'estado': 'Confirmada'
    }
    
    print(f"\n🎉 Reserva {reserva_id} creada para {HUESPEDES[huesped_id]['nombre']} en Hab. {habitacion}.")
    
    # --- Facturación Automática (Relación 1:1) ---
    facturar_reserva(reserva_id, auto_generate=True)


def facturar_reserva(reserva_id=None, auto_generate=False):
    """Función para facturar una reserva y registrar un pago, usando return en lugar de break."""
    
    if reserva_id is None:
        reserva_id = input("Ingrese el ID de la Reserva a facturar (Ej: R0001): ").upper()
    
    if reserva_id not in RESERVAS:
        print(f"❌ Reserva {reserva_id} no encontrada.")
        return

    reserva = RESERVAS[reserva_id]
    huesped = HUESPEDES.get(reserva['id_huesped'], {'nombre': 'Desconocido', 'apellido': ''})
    
    # 1. Buscar o Generar Factura
    factura_id = None
    for fid, fact in FACTURAS.items():
        if fact['id_reserva'] == reserva_id:
            factura_id = fid
            break 
    
    if not factura_id:
        factura_id = generar_id('F')
        FACTURAS[factura_id] = {
            'id_reserva': reserva_id,
            'total_facturado': reserva['total_final'],
            'pagado': 0.0,
            'fecha_generacion': time.strftime("%Y-%m-%d")
        }
        if auto_generate:
            print(f"📝 Factura {factura_id} generada automáticamente.")
            
    
    factura = FACTURAS[factura_id]
    pendiente = factura['total_facturado'] - factura['pagado']
    
    # 2. Presentar Resumen
    print(f"\n--- FACTURA {factura_id} (Reserva {reserva_id}) ---")
    print(f"Huésped: {huesped['nombre']} {huesped['apellido']}")
    print(f"Cargos por Servicios: ${reserva.get('costo_servicios', 0.0):.2f}")
    print(f"Servicios: {', '.join(reserva.get('servicios', ['Ninguno']))}")
    print("-" * 35)
    print(f"Total Facturado: ${factura['total_facturado']:.2f}")
    print(f"Total Pagado: ${factura['pagado']:.2f}")
    print(f"Saldo Pendiente: ${pendiente:.2f}")
    
    # 3. Registrar Pago
    if pendiente > 0:
        # Validación 
        monto_pago = obtener_float_valido(f"Monto a pagar (máx. {pendiente:.2f}, 0 para cancelar): $")
        
        if monto_pago == 0:
            print("Pago cancelado.")
            return 
        
        if monto_pago > pendiente:
            print(f"❗ El monto de pago (${monto_pago:.2f}) excede el saldo pendiente (${pendiente:.2f}). Pago cancelado.")
            return 

        metodo = input("Método de pago: ")
        
        # Simulación de registro de pago
        factura['pagado'] += monto_pago
        pendiente_final = factura['total_facturado'] - factura['pagado']
        
        print(f"\n💰 Pago de ${monto_pago:.2f} registrado por {metodo} el {time.strftime('%Y-%m-%d')}.")
        print(f"Nuevo Saldo Pendiente: ${pendiente_final:.2f}")
        
        if pendiente_final <= 0:
            RESERVAS[reserva_id]['estado'] = 'Pagada'
            print("✅ Factura COMPLETAMENTE PAGADA.")
    else:
        print("\nFactura ya pagada en su totalidad.")

# ------------------------------------
# --- MENÚ PRINCIPAL  ---
# ------------------------------------

def menu_principal():
    """Presenta el menú de opciones al usuario, usando un flag booleano en lugar de break."""
    ejecutando = True 
    while ejecutando:
        print("\n==================================")
        print("  SISTEMA DE GESTIÓN HOTELERA (v1.0)")
        print("==================================")
        print("1. Crear Nueva Reserva (incl. Servicios/Desc.)")
        print("2. Listar Reservas")
        print("3. Registrar Nuevo Huésped")
        print("4. Facturación y Registro de Pago")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            crear_reserva()
        elif opcion == '2':
            listar_reservas()
        elif opcion == '3':
            crear_huesped()
        elif opcion == '4':
            facturar_reserva()
        elif opcion == '5':
            print("Saliendo del sistema. ¡Hasta pronto!")
            ejecutando = False 
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar la aplicación
if __name__ == "__main__":
    menu_principal()