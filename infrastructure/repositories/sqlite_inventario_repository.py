import sqlite3
from domain.entities.inventario import Material

class SQLiteInventarioRepository:
    def __init__(self, db_path):
        self.db_path = db_path
        self._crear_tabla()

    def _crear_tabla(self):
        """
        Crea la tabla de materiales en la base de datos si no existe.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS materiales (
                    nombre TEXT PRIMARY KEY,
                    cantidad_disponible INTEGER,
                    precio REAL
                )
            ''')
            conn.commit()

    def agregar_material(self, material):
        """
        Agrega un nuevo material a la base de datos.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO materiales (nombre, cantidad_disponible, precio)
                VALUES (?, ?, ?)
            ''', (material.nombre, material.cantidad_disponible, material.precio))
            conn.commit()

    def obtener_material(self, nombre):
        """
        Obtiene un material por su nombre.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT nombre, cantidad_disponible, precio FROM materiales WHERE nombre = ?', (nombre,))
            row = cursor.fetchone()
            if row:
                return Material(row[0], row[1], row[2])
        return None

    def actualizar_cantidad(self, nombre, cantidad):
        """
        Actualiza la cantidad disponible de un material.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE materiales
                SET cantidad_disponible = cantidad_disponible + ?
                WHERE nombre = ?
            ''', (cantidad, nombre))
            conn.commit()

    def eliminar_material(self, nombre):
        """
        Elimina un material del inventario.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM materiales WHERE nombre = ?', (nombre,))
            conn.commit()