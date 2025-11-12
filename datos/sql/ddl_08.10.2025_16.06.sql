create table if not exists huesped(
    id INT auto_increment,
    nombre VARCHAR(150) NOT NULL,
    apellido VARCHAR(150) NOT NULL,
    telefono INT NOT NULL,
    email VARCHAR(250) NOT NULL,

    CONSTRAINT pk_huesped PRIMARY KEY (id)   
);
create table if not exists empleado(
    id INT auto_increment,
    nombre VARCHAR(150) NOT NULL,
    apellido VARCHAR(150) NOT NULL,
    telefono INT NOT NULL,
    puesto VARCHAR(50) NOT NULL,
    salario INT NOT NULL,

    CONSTRAINT pk_empleado PRIMARY KEY (id)
);
create table if not exists habitacion(
    id INT auto_increment,
    numero INT NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    precio INT NOT NULL,

    CONSTRAINT pk_habitacion PRIMARY KEY (id)
);
create table if not exists servicio(
    id INT auto_increment,
    nombre VARCHAR(150) NOT NULL,
    precio VARCHAR(150) NOT NULL,

    CONSTRAINT pk_servicio PRIMARY KEY (id) 
);
create table if not exists descuento(
    id INT auto_increment,
    nombre VARCHAR(250) NOT NULL,
    porcentaje INT NOT NULL,

    CONSTRAINT pk_descuento PRIMARY KEY (id)
);
create table if not exists hotel(
    id INT auto_increment,
    nombre VARCHAR(250) NOT NULL,
    direccion VARCHAR(250) NOT NULL,

    CONSTRAINT pk_hotel PRIMARY KEY (id)
);
create table if not exists reserva(
    id INT AUTO_INCREMENT,
    id_huesped INT NOT NULL,
    id_habitacion INT NOT NULL,
    porcentaje_descuento INT NOT NULL,
    precio_servicio INT NOT NULL,
    fecha_entrada DATETIME NOT NULL,
    fecha_salida DATETIME NOT NULL,
    total INT NOT NULL,

    CONSTRAINT pk_reserva PRIMARY KEY (id),
    CONSTRAINT fk_reserva_huesped FOREIGN KEY (id_huesped) REFERENCES huesped(id),
    CONSTRAINT fk_reserva_habitacion FOREIGN KEY (id_habitacion) REFERENCES habitacion(id),
    CONSTRAINT fk_reserva_porcentaje FOREIGN KEY (porcentaje_descuento) REFERENCES descuento(id),
    CONSTRAINT fk_reserva_servicio FOREIGN KEY (precio_servicio) REFERENCES servicio(id)
);
create table if not exists factura(
    id INT auto_increment,
    id_reserva INT NOT NULL,

    CONSTRAINT pk_factura PRIMARY KEY (id),
    CONSTRAINT fk_factura_reserva FOREIGN KEY (id_reserva) REFERENCES reserva(id)
);
create table if not exists pago(
    id INT auto_increment,
    id_factura INT NOT NULL,
    metodo_pago VARCHAR(50) NOT NULL,
    fecha_pago DATETIME NOT NULL, 
    pendiente BOOLEAN NOT NULL,

    CONSTRAINT pk_pago PRIMARY KEY (id),
    CONSTRAINT fk_pago_factura FOREIGN KEY (id_factura) REFERENCES factura(id)
);