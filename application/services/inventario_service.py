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
        
    def registrar_material(self, data):
        return self.inventario_repository.registrar_material(data)
    
    def consultar_cantidad(self, nombre):
        material = self.inventario_repository.obtener_por_nombre(nombre)
        print(material, 'materialll')
        if material is None:
            raise ValueError(f"Material '{nombre}' no encontrado")
        return material

    def actualizar_inventario(self, nombre, cantidad):
        return self.inventario_repository.actualizar_inventario(nombre, cantidad)
    
    def actualizar_precio(self, nombre, precio):
        return self.inventario_repository.actualizar_precio(nombre, precio)
   