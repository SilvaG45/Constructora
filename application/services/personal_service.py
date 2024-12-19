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

    def actualizar_personal(self, personal):
        self.repository.actualizar(personal)

    def eliminar_personal(self, personal_id):
        self.repository.eliminar(personal_id)

    def asignar_a_proyecto(self, data):
       return self.repository.asignar_a_proyecto(data)

    def obtener_proyectos_asignados(self, personal_id):
        personal = self.obtener_personal(personal_id)
        if personal:
            return personal.obtenerProyectosAsignados()
        return None

    def obtener_horas_trabajadas(self, personal_id):
        personal = self.obtener_personal(personal_id)
        if personal:
            return self.repository.obtener_horas_trabajadas(personal_id)
        return 0