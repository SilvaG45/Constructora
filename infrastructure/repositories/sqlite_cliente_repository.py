import sqlite3
from domain.entities.cliente import Cliente

class SQLiteClienteRepository:
    def agregar(self, cliente):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO clientes (id, nombre, direccion, contacto, proyectos) VALUES (?, ?, ?, ?, ?)",
            (cliente.id, cliente.nombre, cliente.direccion, cliente.contacto, cliente.proyectos)
        )
        conn.commit()
        conn.close()

    def obtener_por_id(self, cliente_id):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, direccion, contacto, proyectos FROM clientes WHERE id = ?", (cliente_id,))
        row = cursor.fetchone()
        conn.close()
        return Cliente(*row) if row else None
    
    def listar_todos(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, direccion, contacto, proyectos FROM clientes")
        rows = cursor.fetchall()
        conn.close()
        return [Cliente(*row) for row in rows]