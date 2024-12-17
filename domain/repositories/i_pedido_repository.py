from abc import ABC, abstractmethod

class IPedidoRepository(ABC):
    @abstractmethod
    def agregar(self, pedido):
        pass

    @abstractmethod
    def obtener_por_id(self, pedido_id):
        pass

    @abstractmethod
    def listar_todos(self):
        pass

    @abstractmethod
    def agregar_material_a_pedido(self, pedido_id, material_id, cantidad):
        pass

    @abstractmethod
    def consultar_materiales(self, pedido_id):
        pass
