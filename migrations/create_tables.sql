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

CREATE TABLE IF NOT EXISTS proyectos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    presupuesto_inicial REAL NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_estimacion_fin DATE NOT NULL,
    porcentaje_avance REAL NOT NULL
);
