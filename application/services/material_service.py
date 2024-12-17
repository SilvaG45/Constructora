from domain.repositories.i_material_repository import IMaterialRepository
from infrastructure.repositories.sqlite_material_repository import SQLiteMaterialRepository

class MaterialService:
    def __init__(self):
        self.repository = SQLiteMaterialRepository()

    def registrar_material(self, material):
        self.repository.agregar(material)

    def obtener_material(self, material_id):
        return self.repository.obtener_por_id(material_id)

    def listar_todos(self):
        return self.repository.listar_todos()

    def actualizar_precio(self, material_id, nuevo_precio):
        material = self.obtener_material(material_id)
        if material:
            material.actualizar_precio(nuevo_precio)
            self.repository.actualizar(material)
            return material
        return None

    def consultar_disponibilidad(self, material_id):
        return self.repository.consultar_disponibilidad(material_id)