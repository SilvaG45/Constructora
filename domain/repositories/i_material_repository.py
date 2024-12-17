from abc import ABC, abstractmethod

class IMaterialRepository(ABC):
    @abstractmethod
    def agregar(self, material):
        pass

    @abstractmethod
    def obtener_por_id(self, material_id):
        pass

    @abstractmethod
    def listar_todos(self):
        pass

    @abstractmethod
    def actualizar_precio(self, material_id, nuevo_precio):
        pass

    @abstractmethod
    def consultar_disponibilidad(self, material_id):
        pass