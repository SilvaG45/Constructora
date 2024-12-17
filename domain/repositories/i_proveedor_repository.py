from abc import ABC, abstractmethod

class IProveedorRepository(ABC):
    @abstractmethod
    def agregar(self, proveedor):
        pass

    @abstractmethod
    def obtener_por_id(self, proveedor_id):
        pass

    @abstractmethod
    def listar_todos(self):
        pass

    @abstractmethod
    def registrar_pedido(self, proveedor_id, pedido):
        pass

    @abstractmethod
    def obtener_historial_pedidos(self, proveedor_id):
        pass
