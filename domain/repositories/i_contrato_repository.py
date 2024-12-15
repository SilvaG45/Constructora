from abc import ABC, abstractmethod

class IContratoRepository(ABC):
    @abstractmethod
    def agregar(self, contrato):
        pass

    @abstractmethod
    def obtener_por_id(self, contrato_id):
        pass

    @abstractmethod
    def listar_todos(self):
        pass