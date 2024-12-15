from abc import ABC, abstractmethod

class IProyectoRepository(ABC):
    
    @abstractmethod
    def agregar_proyecto(self, proyecto):  
        pass
    
    @abstractmethod
    def listar_proyectos(self):
        pass
    
    @abstractmethod
    def obtener_proyecto(self, proyecto_id: int):
        pass

    @abstractmethod
    def actualizar_proyecto(self, proyecto):
        pass

    @abstractmethod
    def eliminar_proyecto(self, proyecto_id: int):
        pass

    