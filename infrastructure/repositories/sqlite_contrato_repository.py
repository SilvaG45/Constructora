import sqlite3
from domain.entities.contrato import Contrato

class SQLiteContratoRepository:
    def agregar(self, contrato):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO contratos (id, monto, condiciones, estado, cliente, proyecto) VALUES (?, ?, ?, ?, ?, ?)",
            (contrato.id, contrato.monto, contrato.condiciones, contrato.estado, contrato.cliente, contrato.proyecto)
        )
        conn.commit()
        conn.close()

    def obtener_por_id(self, contrato_id):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, monto, condiciones, estado, cliente, proyecto FROM contratos WHERE id = ?", (contrato_id,))
        row = cursor.fetchone()
        conn.close()
        return Contrato(*row) if row else None
    
    def listar_todos(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, monto, condiciones, estado, cliente, proyecto FROM contratos")
        rows = cursor.fetchall()
        conn.close()
        return [Contrato(*row) for row in rows]