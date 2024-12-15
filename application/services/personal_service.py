from domain.repositories.i_personal_repository import IPersonalRepository
from infrastructure.repositories.sqlite_personal_repository import SQLitePersonalRepository

class PersonalService:
    def __init__(self):
        self.repository = SQLitePersonalRepository()

    def registrar_personal(self, personal):
        self.repository.agregar(personal)

    def obtener_personal(self, personal_id):
        return self.repository.obtener_por_id(personal_id)

    def listar_todos(self):
        return self.repository.listar_todos()
