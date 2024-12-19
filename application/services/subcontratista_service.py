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

    def actualizar_subcontratista(self, subcontratista):
        self.repository.actualizar(subcontratista)

    def eliminar_subcontratista(self, subcontratista_id):
        self.repository.eliminar(subcontratista_id)

    def asignar_a_proyecto(self, data):
       return self.repository.asignar_a_proyecto(data)

    def liberar_de_proyecto(self, subcontratista_id, proyecto):
        subcontratista = self.obtener_subcontratista(subcontratista_id)
        if subcontratista:
            if subcontratista.liberarDeProyecto(proyecto):
                self.actualizar_subcontratista(subcontratista)
                return subcontratista
        return None

    def obtener_proyectos_asignados(self, subcontratista_id):
        subcontratista = self.obtener_subcontratista(subcontratista_id)
        if subcontratista:
            return subcontratista.obtenerProyectosAsignados()
        return None

    def obtener_horas_trabajadas(self, subcontratista_id):
        subcontratista = self.obtener_subcontratista(subcontratista_id)
        if subcontratista:
            return self.repository.obtener_horas_trabajadas(subcontratista_id)
        return 0
