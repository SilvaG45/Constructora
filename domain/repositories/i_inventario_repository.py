from abc import ABC, abstractmethod

class IInventarioRepository(ABC):
    @abstractmethod
    def agregar_inventario(self):
        pass

    @abstractmethod
    def obtener_inventario(self, inventario_id):
        pass

    @abstractmethod
    def listar_materiales(self):
        pass

    @abstractmethod
    def actualizar_inventario(self, nombre, cantidad):
        pass

    @abstractmethod
    def registrar_material(self, data):
        pass

    @abstractmethod
    def obtener_por_nombre(self, nombre):
        pass

    @abstractmethod
    def actualizar_precio(self, nombre, precio):
        pass