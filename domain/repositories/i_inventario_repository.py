from abc import ABC, abstractmethod

class IInventarioRepository(ABC):
    @abstractmethod
    def agregar_material(self, material):
        pass

    @abstractmethod
    def obtener_material(self, nombre):
        pass

    @abstractmethod
    def actualizar_cantidad(self, nombre, cantidad):
        pass

    @abstractmethod
    def eliminar_material(self, nombre):
        pass