import sqlite3
from domain.entities.inventario import Inventario

class SQLiteInventarioRepository:
    def __init__(self):
        self.conn = sqlite3.connect('database.db', check_same_thread=False)

# agregar inventario 
    def agregar_inventario(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO inventario DEFAULT VALUES"
        )
        self.conn.commit()
        
    def obtener_inventario(self, inventario_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM inventario WHERE inventario_id = ?", (inventario_id,))
        row = cursor.fetchone()
        if row:
            return Inventario(
                id=row[0],
            )  
        return None
    
    def listar_inventarios(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM inventario")
        rows = cursor.fetchall()
        return [
            Inventario(
                id=row[0],
            ) 
            for row in rows
        ]
    
    def listar_materiales(self):
        # en inventario_material
        pass
    
    def actualizar_inventario(self, nombre, cantidad):
        print(nombre, cantidad, 'nombre y cantidad')
        # en inventario_material
        cursor= self.conn.cursor()
        cursor.execute(
            "UPDATE inventario_material SET cantidad = ? WHERE material_id = (SELECT material_id FROM materiales WHERE UPPER(nombre) = UPPER(?))",
            (cantidad, nombre)
        )
        self.conn.commit()
    
    def registrar_material(self, data):
        print(data, 'data en repositorio')
        # en inventario_material
        cursor= self.conn.cursor()
        cursor.execute(
            "INSERT INTO inventario_material (inventario_id, material_id, cantidad) VALUES (?, ?, ?)",
            (data['inventario_id'], data['material_id'], data['cantidad'])
        )
        self.conn.commit()
            
    def obtener_por_nombre(self, nombre):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT m.material_id, m.nombre, m.precio, im.cantidad
            FROM materiales m
            INNER JOIN inventario_material im ON m.material_id = im.material_id
            WHERE UPPER(m.nombre) = UPPER(?)
        """, (nombre,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return {
                "id": row[0],
                "nombre": row[1],
                "precio": row[2],
                "cantidad": row[3]
            }
        return None
    
    def actualizar_precio(self, nombre, precio):
        cursor= self.conn.cursor()
        cursor.execute(
            "UPDATE materiales SET precio = ? WHERE UPPER(nombre) = UPPER(?)",
            (precio, nombre)
        )
        self.conn.commit()