CREATE TABLE IF NOT EXISTS personal (
    personal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    rol TEXT NOT NULL,
    horas_trabajadas INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS subcontratistas (
    subcontratista_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    especialidad TEXT NOT NULL,
    disponible BOOLEAN DEFAULT 1
);


CREATE TABLE IF NOT EXISTS clientes (
    cliente_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    direccion TEXT NOT NULL,
    contacto TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS proyectos (
    proyecto_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    presupuesto_inicial REAL NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_estimacion_fin DATE NOT NULL,
    porcentaje_avance REAL NOT NULL
    contrato_id INTEGER, 
    FOREIGN KEY (contrato_id) REFERENCES contratos (id)
);

CREATE TABLE IF NOT EXISTS contratos (
    contrato_id INTEGER PRIMARY KEY AUTOINCREMENT,
    monto REAL NOT NULL,
    condiciones TEXT NOT NULL,
    estado TEXT NOT NULL,
    cliente_id INTEGER NOT NULL,
    proyecto_id INTEGER,
    FOREIGN KEY (cliente) REFERENCES clientes(id)
    FOREIGN KEY (proyecto) REFERENCES proyectos(id)
);

CREATE TABLE IF NOT EXISTS proveedores (
    proveedor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS materiales (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    cantidad_disponible INTEGER NOT NULL,
    precio REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS pedidos (
    pedido_id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_pedido TEXT NOT NULL,
    fecha_pedido TEXT NOT NULL,
    proveedor_id INTEGER NOT NULL,
    FOREIGN KEY (proveedor_id) REFERENCES proveedores (proveedor_id)
);

CREATE TABLE IF NOT EXISTS pedido_material (
    pedido_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    PRIMARY KEY (pedido_id, material_id),
    FOREIGN KEY (pedido_id) REFERENCES pedidos (pedido_id),
    FOREIGN KEY (material_id) REFERENCES materiales (material_id)
);

CREATE TABLE IF NOT EXISTS subcontratista_proyectos (
    subcontratista_id INTEGER NOT NULL,
    proyecto_id INTEGER NOT NULL,
    FOREIGN KEY (subcontratista_id) REFERENCES subcontratistas (subcontratista_id),
    FOREIGN KEY (proyecto_id) REFERENCES proyectos (proyecto_id)
);

CREATE TABLE IF NOT EXISTS proyecto_materiales (
    proyecto_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    PRIMARY KEY (proyecto_id, material_id),
    FOREIGN KEY (proyecto_id) REFERENCES proyectos (proyecto_id),
    FOREIGN KEY (material_id) REFERENCES materiales (material_id)
);

CREATE TABLE IF NOT EXISTS proyecto_personal (
    proyecto_id INTEGER NOT NULL,
    personal_id INTEGER NOT NULL,
    horas_trabajadas INTEGER NOT NULL,
    PRIMARY KEY (proyecto_id, personal_id),
    FOREIGN KEY (proyecto_id) REFERENCES proyectos (proyecto_id),
    FOREIGN KEY (personal_id) REFERENCES personal (personal_id)
);

CREATE TABLE IF NOT EXISTS cliente_proyectos (
    cliente_id INTEGER NOT NULL,
    proyecto_id INTEGER NOT NULL,
    PRIMARY KEY (cliente_id, proyecto_id),
    FOREIGN KEY (cliente_id) REFERENCES clientes (cliente_id),
    FOREIGN KEY (proyecto_id) REFERENCES proyectos (proyecto_id)
);