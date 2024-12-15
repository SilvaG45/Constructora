import sqlite3
from domain.entities.personal import Personal

class SQLitePersonalRepository:
    def agregar(self, personal):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO personal (id, nombre, rol, horas_trabajadas) VALUES (?, ?, ?, ?)",
            (personal.id, personal.nombre, personal.rol, personal.horas_trabajadas)
        )
        conn.commit()
        conn.close()

    def obtener_por_id(self, personal_id):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, rol, horas_trabajadas FROM personal WHERE id = ?", (personal_id,))
        row = cursor.fetchone()
        conn.close()
        return Personal(*row) if row else None

    def listar_todos(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, rol, horas_trabajadas FROM personal")
        rows = cursor.fetchall()
        conn.close()
        return [Personal(*row) for row in rows]
