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