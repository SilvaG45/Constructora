import sqlite3
from domain.entities.proveedor import Proveedor
from domain.entities.pedido import Pedido

class SQLiteProveedorRepository:
    def __init__(self):
        self.conn = sqlite3.connect('database.db', check_same_thread=False)

    def agregar(self, proveedor):
        print(proveedor, 'proveedor en repositorio')
        print(proveedor.nombre, 'nombre en repositorio')
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO proveedores (nombre) VALUES (?)",
            (proveedor.nombre,)
        )
        proveedor.id = cursor.lastrowid
        self.conn.commit()
        cursor.close()

    def obtener_por_id(self, proveedor_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM proveedores WHERE proveedor_id = ?", (proveedor_id,))
        row = cursor.fetchone()
        if row:
            return Proveedor(id=row[0], nombre=row[1])
        return None

    def listar_todos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM proveedores")
        rows = cursor.fetchall()
        return [Proveedor(id=row[0], nombre=row[1]) for row in rows]

    def obtener_historial_pedidos(self, proveedor_id):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT pedido_id, proveedor_id, fecha_pedido
            FROM pedidos
            WHERE proveedor_id = ?
            ORDER BY fecha_pedido DESC
        """, (proveedor_id,))
        rows = cursor.fetchall()
        pedidos = [Pedido(id=row[0], proveedor_id=row[1], fecha_pedido=row[2]) for row in rows]
        cursor.close()
        return pedidos