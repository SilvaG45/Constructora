import sqlite3
from domain.entities.proveedor import Proveedor

class SQLiteProveedorRepository:
    def __init__(self):
        self.conn = sqlite3.connect('database.db', check_same_thread=False)

    def agregar(self, proveedor):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO proveedores (id, nombre) VALUES (?, ?)",
            (proveedor.id, proveedor.nombre)
        )
        self.conn.commit()

    def obtener_por_id(self, proveedor_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM proveedores WHERE id = ?", (proveedor_id,))
        row = cursor.fetchone()
        if row:
            return Proveedor(id=row[0], nombre=row[1])
        return None

    def listar_todos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM proveedores")
        rows = cursor.fetchall()
        return [Proveedor(id=row[0], nombre=row[1]) for row in rows]

    def registrar_pedido(self, proveedor_id, pedido):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO pedidos (id, numero_pedido, fecha_pedido, proveedor_id) VALUES (?, ?, ?, ?)",
            (pedido.id, pedido.numero_pedido, pedido.fecha_pedido, proveedor_id)
        )
        self.conn.commit()

    def obtener_historial_pedidos(self, proveedor_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM pedidos WHERE proveedor_id = ?", (proveedor_id,))
        rows = cursor.fetchall()
        return [
            {"id": row[0], "numero_pedido": row[1], "fecha_pedido": row[2]}
            for row in rows
        ]