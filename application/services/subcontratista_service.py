from domain.repositories.i_subcontratista_repository import ISubcontratistaRepository
from infrastructure.repositories.sqlite_subcontratista_repository import SQLiteSubcontratistaRepository

class SubcontratistaService:
    def __init__(self):
        self.repository = SQLiteSubcontratistaRepository()

    def registrar_subcontratista(self, subcontratista):
        self.repository.agregar(subcontratista)

    def obtener_subcontratista(self, subcontratista_id):
        return self.repository.obtener_por_id(subcontratista_id)

    def listar_todos(self):
        return self.repository.listar_todos()
