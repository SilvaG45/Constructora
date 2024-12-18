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

    @abstractmethod
    def registrar_contrato(self, infoContrato, cliente_id):
        pass

    @abstractmethod
    def actualizar_estado(self, estado):
        pass