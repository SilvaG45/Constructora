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
                materiales=row[1],
            )  
        return None
    
    def listar_materiales(self):
        # en inventario_material
        pass
    
    def actualizar_inventario(self, nombre, cantidad):
        # en inventario_material
        pass
    