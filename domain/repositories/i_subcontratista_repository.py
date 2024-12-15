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

    @abstractmethod
    def asignar_a_proyecto(self, subcontratista_id, proyecto_id):
        """Asigna un subcontratista a un proyecto."""
        pass

    @abstractmethod
    def liberar_de_proyecto(self, subcontratista_id, proyecto_id):
        """Libera un subcontratista de un proyecto."""
        pass

    @abstractmethod
    def obtener_proyectos_asignados(self, subcontratista_id):
        """Obtiene los proyectos asignados a un subcontratista."""
        pass
