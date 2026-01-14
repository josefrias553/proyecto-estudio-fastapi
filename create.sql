CREATE TABLE estados (
    id_estado SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE ciudades (
    id_ciudad SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_estado INT NOT NULL,
    CONSTRAINT fk_ciudad_estado
        FOREIGN KEY (id_estado)
        REFERENCES estados (id_estado)
);

CREATE TABLE supermercados (
    id_supermercado SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    id_ciudad INT NOT NULL,
    CONSTRAINT fk_supermercado_ciudad
        FOREIGN KEY (id_ciudad)
        REFERENCES ciudades (id_ciudad)
);


CREATE TABLE vendedores (
    id_vendedor SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
);


CREATE TABLE representantes_compras (
    id_representante SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL
);


CREATE TABLE categorias (
    id_categoria SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE productos (
    id_producto SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    presentacion VARCHAR(100) NOT NULL,
    precio_unitario_usd NUMERIC(10,2) NOT NULL CHECK (precio_unitario_usd >= 0),
    id_categoria INT NOT NULL,
    CONSTRAINT fk_producto_categoria
        FOREIGN KEY (id_categoria)
        REFERENCES categorias (id_categoria)
);

CREATE TABLE formas_pago (
    id_forma_pago SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);


CREATE TABLE ordenes (
    id_orden SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    id_vendedor INT NOT NULL,
    id_supermercado INT NOT NULL,
    id_representante INT NOT NULL,
    id_forma_pago INT NOT NULL,
    CONSTRAINT fk_orden_vendedor
        FOREIGN KEY (id_vendedor)
        REFERENCES vendedores (id_vendedor),
    CONSTRAINT fk_orden_supermercado
        FOREIGN KEY (id_supermercado)
        REFERENCES supermercados (id_supermercado),
    CONSTRAINT fk_orden_representante
        FOREIGN KEY (id_representante)
        REFERENCES representantes_compras (id_representante),
    CONSTRAINT fk_orden_forma_pago
        FOREIGN KEY (id_forma_pago)
        REFERENCES formas_pago (id_forma_pago)
);

CREATE TABLE detalle_orden (
    id_detalle SERIAL PRIMARY KEY,
    id_orden INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad_comprada INT NOT NULL CHECK (cantidad_comprada > 0),
    valor_total_usd NUMERIC(12,2) NOT NULL CHECK (valor_total_usd >= 0),
    CONSTRAINT fk_detalle_orden
        FOREIGN KEY (id_orden)
        REFERENCES ordenes (id_orden),
    CONSTRAINT fk_detalle_producto
        FOREIGN KEY (id_producto)
        REFERENCES productos (id_producto),
    CONSTRAINT uq_orden_producto UNIQUE (id_orden, id_producto)
);
