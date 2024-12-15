import sqlite3
from domain.entities.subcontratista import Subcontratista

class SQLiteSubcontratistaRepository:
    def agregar(self, subcontratista):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO subcontratistas (id, nombre, especialidad, disponible) VALUES (?, ?, ?, ?)",
            (subcontratista.id, subcontratista.nombre, subcontratista.especialidad, subcontratista.disponible)
        )
        conn.commit()
        conn.close()

    def obtener_por_id(self, subcontratista_id):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, especialidad, disponible FROM subcontratistas WHERE id = ?", (subcontratista_id,))
        row = cursor.fetchone()
        conn.close()
        return Subcontratista(*row) if row else None

    def listar_todos(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, especialidad, disponible FROM subcontratistas")
        rows = cursor.fetchall()
        conn.close()
        return [Subcontratista(*row) for row in rows]
