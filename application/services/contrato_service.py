from domain.repositories.i_contrato_repository import IContratoRepository
from infrastructure.repositories.sqlite_contrato_repository import SQLiteContratoRepository

class ContratoService:
    def __init__(self):
        self.repository = SQLiteContratoRepository()

    def registrar_contrato(self, contrato):
        self.repository.agregar(contrato)

    def obtener_contrato(self, contrato_id):
        return self.repository.obtener_por_id(contrato_id)
    
    def listar_todos(self):
        return self.repository.listar_todos()