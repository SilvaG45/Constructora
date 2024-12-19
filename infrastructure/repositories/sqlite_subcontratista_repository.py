import sqlite3
from domain.entities.subcontratista import Subcontratista

class SQLiteSubcontratistaRepository:
    def __init__(self):
        self.conn = sqlite3.connect('database.db', check_same_thread=False)

    def agregar(self, subcontratista):
        print(subcontratista)
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO subcontratistas (nombre, especialidad, disponible) VALUES (?, ?, ?)",
            (subcontratista.nombre, subcontratista.especialidad, subcontratista.disponible)
        )
        self.conn.commit()

    def obtener_por_id(self, subcontratista_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM subcontratistas WHERE subcontratista_id = ?", (subcontratista_id,))
        row = cursor.fetchone()
        if row:
            return Subcontratista(
                id=row[0],
                nombre=row[1],
                especialidad=row[2],
                disponible=bool(row[3])
            )
        return None

    def listar_todos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM subcontratistas")
        rows = cursor.fetchall()
        return [
            Subcontratista(id=row[0], nombre=row[1], especialidad=row[2], disponible=bool(row[3]))
            for row in rows
        ]

    def actualizar(self, subcontratista):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE subcontratistas SET nombre = ?, especialidad = ?, disponible = ? WHERE subcontratista_id = ?",
            (subcontratista.nombre, subcontratista.especialidad, subcontratista.disponible, subcontratista.id)
        )
        self.conn.commit()

    def eliminar(self, subcontratista_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM subcontratistas WHERE subcontratista_id = ?", (subcontratista_id,))
        self.conn.commit()

    def asignar_a_proyecto(self, data):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO subcontratista_proyectos (subcontratista_id, proyecto_id, horas_trabajadas) VALUES (?, ?, ?)",
            (data['subcontratista_id'], data['proyecto_id'], data['horas_trabajadas'])
        )
        self.conn.commit()

    def obtener_proyectos_asignados(self, subcontratista_id):
        """Devuelve los proyectos asignados a un subcontratista."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT p.proyecto_id, p.nombre, p.fecha_inicio, p.fecha_estimacion_fin "
            "FROM proyectos p "
            "INNER JOIN subcontratista_proyectos sp ON p.proyecto_id = sp.proyecto_id "
            "WHERE sp.subcontratista_id = ?",
            (subcontratista_id,)
        )
        rows = cursor.fetchall()
        return [
            {
                "id": row[0],
                "nombre": row[1],
                "fecha_inicio": row[4],
                "fecha_estimacion_fin": row[5]
            }
            for row in rows
        ]
