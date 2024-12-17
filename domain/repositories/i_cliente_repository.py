from abc import ABC, abstractmethod

class IClienteRepository(ABC):
    @abstractmethod
    def agregar(self, cliente):
        pass

    @abstractmethod
    def obtener_por_id(self, cliente_id):
        pass

    @abstractmethod
    def listar_todos(self):
        pass

    @abstractmethod
    def coincide_con(self, infoCliente):
        """Verifica si la información del cliente coincide con los atributos."""
        pass

    @abstractmethod
    def agregar_cliente(self, infoCliente):
        """Agrega un cliente."""
        pass

    @abstractmethod
    def obtener_proyectos(self, cliente_id):
        """Devuelve una lista de proyectos asociados al cliente."""
        pass