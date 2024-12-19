import sqlite3
from domain.entities.proyecto import Proyecto
from icecream import ic

class SQLiteProyectoRepository:
    def agregar(self, proyecto):
        print(proyecto)
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO proyectos (nombre, presupuesto_inicial, fecha_inicio, fecha_estimacion_fin, porcentaje_avance) VALUES (?, ?, ?, ?, ?)",
            (proyecto.nombre, proyecto.presupuesto_inicial, proyecto.fecha_inicio, proyecto.fecha_estimacion_fin, proyecto.porcentaje_avance)
        )
        proyecto.id = cursor.lastrowid
        conn.commit()
         # Verificar lo que se guardó
        cursor.execute("SELECT * FROM proyectos WHERE proyecto_id = ?", (cursor.lastrowid,))
        row = cursor.fetchone()
        ic(row)
        conn.close()

    def obtener_por_id(self, proyecto_id):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT proyecto_id, nombre, presupuesto_inicial, fecha_inicio, fecha_estimacion_fin, porcentaje_avance FROM proyectos WHERE proyecto_id = ?", (proyecto_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            proyecto = Proyecto(id= row[0], nombre=row[1], presupuesto_inicial=row[2], fecha_inicio=row[3], fecha_estimacion_fin=row[4], porcentaje_avance=row[5])
            return proyecto
        return None

    def listar_todos(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT proyecto_id, nombre, presupuesto_inicial, fecha_inicio, fecha_estimacion_fin, porcentaje_avance FROM proyectos")
        rows = cursor.fetchall()
        ic(rows)
        conn.close()
        proyectos = []
        for row in rows:
            proyecto = Proyecto(id= row[0], nombre=row[1], presupuesto_inicial=row[2], fecha_inicio=row[3], fecha_estimacion_fin=row[4], porcentaje_avance=row[5])
            proyectos.append(proyecto)
        return proyectos
    
    def actualizar(self, proyecto):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE proyectos SET nombre = ?, presupuesto_inicial = ?, fecha_inicio = ?, fecha_estimacion_fin = ?, porcentaje_avance = ? WHERE proyecto_id = ?",
            (proyecto.nombre, proyecto.presupuesto_inicial, proyecto.fecha_inicio, proyecto.fecha_estimacion_fin, proyecto.porcentaje_avance, proyecto.id)
        )
        conn.commit()
        conn.close()
        
    def cambiar_fecha_fin(self, proyecto_id, data):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE proyectos SET fecha_estimacion_fin = ? WHERE proyecto_id = ?",
            (data.get("fecha_estimacion_fin"), proyecto_id)
        )
        conn.commit()
        conn.close()
                
    def cambiar_presupuesto(self, proyecto_id, data):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE proyectos SET presupuesto_inicial = ? WHERE proyecto_id = ?",
            (data.get("presupuesto_inicial"), proyecto_id)
        )
        conn.commit()
        conn.close()
        
    def eliminar(self, proyecto_id):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM proyectos WHERE proyecto_id = ?", (proyecto_id,))
        conn.commit()
        conn.close()
        
    def agregar_materiales(self, data):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO proyecto_materiales (proyecto_id, material_id, cantidad) VALUES (?, ?, ?)",
            (data['proyecto_id'], data['material_id'], data['cantidad'])
        )
        conn.commit()
        conn.close()
        
    def obtener_materiales_proyecto(self, proyecto_id):
        """Obtiene los materiales necesarios para un proyecto y sus cantidades disponibles."""
        conn = sqlite3.connect('database.db')
        cursor= conn.cursor()
        query = """
            SELECT pm.material_id, pm.cantidad AS requerida, im.cantidad AS disponible
            FROM proyecto_materiales pm
            JOIN inventario_material im ON pm.material_id = im.material_id
            WHERE pm.proyecto_id = ?
        """
        cursor.execute(query, (proyecto_id,))
        return cursor.fetchall()
    
    def descontar_materiales(self, proyecto_id):
        """Descuenta los materiales del inventario después de verificar su disponibilidad."""
        cursor = self.conn.cursor()
        query = """
            UPDATE inventario_material
            SET cantidad = cantidad - (
                SELECT pm.cantidad
                FROM proyecto_materiales pm
                WHERE pm.material_id = inventario_material.material_id
                AND pm.proyecto_id = ?
            )
            WHERE material_id IN (
                SELECT material_id
                FROM proyecto_materiales
                WHERE proyecto_id = ?
            )
        """
        cursor.execute(query, (proyecto_id, proyecto_id))
        self.conn.commit()
        
        
    def verificar_disponibilidad_materiales(self, proyecto_id):
        cursor = self.conn.cursor()
        query = """
            SELECT pm.material_id, pm.cantidad, im.cantidad AS disponible
            FROM proyecto_materiales pm
            JOIN inventario_material im ON pm.material_id = im.material_id
            WHERE pm.proyecto_id = ?
        """
        cursor.execute(query, (proyecto_id,))
        materiales = cursor.fetchall()

        # Verificar si todos los materiales tienen suficiente cantidad
        for material in materiales:
            if material[1] > material[2]:  # Cantidad requerida > Cantidad disponible
                return False, material[0]  # Retornar False y el ID del material insuficiente
        return True, None
