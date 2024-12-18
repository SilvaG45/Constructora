from infrastructure.repositories.sqlite_inventario_repository import SQLiteInventarioRepository


class InventarioService:
    def __init__(self):
        self.inventario_repository = SQLiteInventarioRepository()
        
    def agregar_inventario(self):
        return self.inventario_repository.agregar_inventario()
    
    def obtener_inventario(self, inventario_id):
        return self.inventario_repository.obtener_por_id(inventario_id)
    
    def listar_materiales(self):
        return self.inventario_repository.listar_materiales()
    
    def actualizar_inventario(self, nombre, cantidad):
        return self.inventario_repository.actualizar_inventario(nombre, cantidad)

   