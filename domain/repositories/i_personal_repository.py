from abc import ABC, abstractmethod

class IPersonalRepository(ABC):
    @abstractmethod
    def agregar(self, personal):
        pass

    @abstractmethod
    def obtener_por_id(self, personal_id):
        pass

    @abstractmethod
    def listar_todos(self):
        pass
