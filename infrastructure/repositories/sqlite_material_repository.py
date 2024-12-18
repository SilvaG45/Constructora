import sqlite3
from domain.entities.material import Material

class SQLiteMaterialRepository:
    def __init__(self):
        self.conn = sqlite3.connect('database.db', check_same_thread=False)

    def agregar(self, material):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO materiales (nombre, cantidad_disponible, precio) VALUES (?, ?, ?)",
            (material.nombre, material.cantidad_disponible, material.precio)
        )
        material.id = cursor.lastrowid
        self.conn.commit()

    def obtener_por_id(self, material_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM materiales WHERE id = ?", (material_id,))
        row = cursor.fetchone()
        if row:
            return Material(
                id=row[0],
                nombre=row[1],
                cantidad_disponible=row[2],
                precio=row[3]
            )
        return None

    def listar_todos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM materiales")
        rows = cursor.fetchall()
        return [
            Material(id=row[0], nombre=row[1], cantidad_disponible=row[2], precio=row[3])
            for row in rows
        ]

    def actualizar_precio(self, material_id, nuevo_precio):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE materiales SET precio = ? WHERE id = ?",
            (nuevo_precio, material_id)
        )
        self.conn.commit()

    def consultar_disponibilidad(self, material_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT cantidad_disponible FROM materiales WHERE id = ?", (material_id,))
        row = cursor.fetchone()
        if row:
            return row[0] > 0
        return False