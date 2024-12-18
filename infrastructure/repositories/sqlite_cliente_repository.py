import sqlite3
from domain.entities.cliente import Cliente

class SQLiteClienteRepository:
    def __init__(self):
        self.conn = sqlite3.connect('database.db', check_same_thread=False)

    def agregar(self, cliente):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO clientes (nombre, direccion, contacto) VALUES (?, ?, ?)",
            (cliente.nombre, cliente.direccion, cliente.contacto)
        )
        cliente.id = cursor.lastrowid
        self.conn.commit()

    def obtener_por_id(self, cliente_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM clientes WHERE cliente_id = ?", (cliente_id,))
        row = cursor.fetchone()
        if row:
            return Cliente(
                id=row[0],
                nombre=row[1],
                direccion=row[2],
                contacto=row[3],
                proyectos=row[4]
            )  
        return None
    
    def listar_todos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        rows = cursor.fetchall()
        return [
            Cliente(
                id=row[0],
                nombre=row[1],
                direccion=row[2],
                contacto=row[3],
                proyectos=row[4]
            ) 
            for row in rows
        ]
    
    def coincide_con(self, infoCliente):
        cursor = self.conn.cursor()
        query = "SELECT * FROM clientes WHERE nombre = ? OR direccion = ? OR contacto = ?"
        cursor.execute(query, (infoCliente.get("nombre"), infoCliente.get("direccion"), infoCliente.get("contacto")))
        rows = cursor.fetchall()
        return [
            Cliente(
                id=row[0],
                nombre=row[1],
                direccion=row[2],
                contacto=row[3],
                proyectos=row[4].split(",") if row[4] else []
            ) 
            for row in rows
        ]

    def agregar_cliente(self, infoCliente):
        cliente = Cliente(
            id=infoCliente["id"],  
            nombre=infoCliente["nombre"],
            direccion=infoCliente["direccion"],
            contacto=infoCliente["contacto"],
            proyectos=infoCliente.get("proyectos", [])
        )
        self.agregar(cliente)
        return True