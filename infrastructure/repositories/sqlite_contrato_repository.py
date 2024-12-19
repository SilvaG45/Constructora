import sqlite3
from domain.entities.contrato import Contrato

class SQLiteContratoRepository:
    def __init__(self):
        self.conn = sqlite3.connect('database.db', check_same_thread=False)

    def agregar(self, contrato):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO contratos (monto, condiciones, estado, cliente_id, proyecto_id) VALUES (?, ?, ?, ?, ?)",
            (contrato.monto, contrato.condiciones, contrato.estado, contrato.cliente.id, contrato.proyecto.id)
        )
        contrato.id = cursor.lastrowid
        self.conn.commit()

    def obtener_por_id(self, contrato_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM contratos WHERE contrato_id = ?", (contrato_id,))
        row = cursor.fetchone()
        if row:
            return Contrato(
                id=row[0],
                monto=row[1],
                condiciones=row[2],
                estado=row[3],
                cliente=row[4],
                proyecto=row[5]
            )  
        return None
    
    def listar_todos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM contratos")
        rows = cursor.fetchall()
        print(rows, 'rows')
        return [
            Contrato(
                id=row[0],
                monto=row[1],
                condiciones=row[2],
                estado=row[3],
                cliente=row[4],
                proyecto=row[5],
                
            ) 
            for row in rows
        ]

    def actualizar_estado(self, contrato_id, estado):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE contratos SET estado = ? WHERE contrato_id = ?",
            (estado, contrato_id)
        )
        self.conn.commit()