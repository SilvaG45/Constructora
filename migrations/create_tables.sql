CREATE TABLE IF NOT EXISTS personal (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    rol TEXT NOT NULL,
    horas_trabajadas INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS subcontratistas (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    especialidad TEXT NOT NULL,
    disponible BOOLEAN DEFAULT 1
);

CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    direccion TEXT NOT NULL,
    contacto TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS contratos (
    id INTEGER PRIMARY KEY,
    monto REAL NOT NULL,
    condiciones TEXT NOT NULL,
    estado TEXT NOT NULL,
    cliente INTEGER NOT NULL,
    /*proyecto INTEGER,*/
    FOREIGN KEY (cliente) REFERENCES clientes(id)
    /*FOREIGN KEY (proyecto) REFERENCES proyectos(id)*/
);