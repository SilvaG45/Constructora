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

    @abstractmethod
    def asignar_a_proyecto(self, personal_id, proyecto_id):
        """Asigna un personal a un proyecto."""
        pass

    @abstractmethod
    def obtener_proyectos_asignados(self, personal_id):
        """Obtiene los proyectos asignados a un personal."""
        pass
