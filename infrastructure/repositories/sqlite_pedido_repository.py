import sqlite3
from domain.entities.pedido import Pedido

class SQLitePedidoRepository:
    def __init__(self):
        self.conn = sqlite3.connect('database.db', check_same_thread=False)

    def agregar(self, pedido):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO pedidos (id, numero_pedido, fecha_pedido, proveedor_id) VALUES (?, ?, ?, ?)",
            (pedido.id, pedido.numero_pedido, pedido.fecha_pedido, pedido.proveedor_id)
        )
        self.conn.commit()

    def obtener_por_id(self, pedido_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM pedidos WHERE id = ?", (pedido_id,))
        row = cursor.fetchone()
        if row:
            return Pedido(
                id=row[0],
                numero_pedido=row[1],
                fecha_pedido=row[2],
                proveedor_id=row[3]
            )
        return None

    def listar_todos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM pedidos")
        rows = cursor.fetchall()
        return [
            Pedido(
                id=row[0],
                numero_pedido=row[1],
                fecha_pedido=row[2],
                proveedor_id=row[3]
            )
            for row in rows
        ]

    def agregar_material_a_pedido(self, pedido_id, material_id, cantidad):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO pedido_material (pedido_id, material_id, cantidad) VALUES (?, ?, ?)",
            (pedido_id, material_id, cantidad)
        )
        self.conn.commit()

    def consultar_materiales(self, pedido_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT m.id, m.nombre, pm.cantidad "
            "FROM materiales m "
            "INNER JOIN pedido_material pm ON m.id = pm.material_id "
            "WHERE pm.pedido_id = ?",
            (pedido_id,)
        )
        rows = cursor.fetchall()
        return [
            {"id": row[0], "nombre": row[1], "cantidad": row[2]}
            for row in rows
        ]