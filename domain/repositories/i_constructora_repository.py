from abc import ABC, abstractmethod
    
class IConstructoraRepository(ABC):
    
    @abstractmethod
    def agregar_constructora(self, constructora):
        pass
    
    @abstractmethod
    def listar_constructoras(self):
        pass
    
    @abstractmethod
    def obtener_constructora(self, constructora_id: int):
        pass

    @abstractmethod
    def actualizar_constructora(self, constructora):
        pass

    @abstractmethod
    def eliminar_constructora(self, constructora_id: int):
        pass

   