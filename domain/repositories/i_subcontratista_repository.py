from abc import ABC, abstractmethod

class ISubcontratistaRepository(ABC):
    @abstractmethod
    def agregar(self, subcontratista):
        pass

    @abstractmethod
    def obtener_por_id(self, subcontratista_id):
        pass

    @abstractmethod
    def listar_todos(self):
        pass
