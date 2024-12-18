from domain.entities.material import Material

class InventarioService:
    def __init__(self, inventario_repository):
        self.inventario_repository = inventario_repository

    def registrar_material(self, nombre, cantidad, precio):
        """
        Registra un nuevo material en el inventario.
        """
        material_existente = self.inventario_repository.obtener_material(nombre)
        if material_existente:
            raise ValueError(f"El material '{nombre}' ya existe en el inventario.")
        nuevo_material = Material(nombre, cantidad, precio)
        self.inventario_repository.agregar_material(nuevo_material)

    def consultar_material(self, nombre):
        """
        Consulta un material específico en el inventario.
        """
        material = self.inventario_repository.obtener_material(nombre)
        if not material:
            raise ValueError(f"El material '{nombre}' no existe en el inventario.")
        return material

    def verificar_inventario(self, nombre, cantidad):
        """
        Verifica si hay suficiente cantidad de un material en el inventario.
        """
        material = self.consultar_material(nombre)
        return material.cantidad_disponible >= cantidad

    def actualizar_inventario(self, nombre, cantidad):
        """
        Actualiza la cantidad disponible de un material.
        """
        material = self.consultar_material(nombre)
        self.inventario_repository.actualizar_cantidad(nombre, cantidad)