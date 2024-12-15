from domain.repositories.i_proyecto_repository import IProyectoRepository
from infrastructure.repositories.sqlite_proyecto_repository import SQLiteProyectoRepository

class ProyectoService:
    def __init__(self):
        self.repository = SQLiteProyectoRepository()

    def registrar_proyecto(self, proyecto):
        self.repository.agregar(proyecto)

    def obtener_proyecto(self, proyecto_id):
        return self.repository.obtener_por_id(proyecto_id)

    def listar_todos(self):
        return self.repository.listar_todos()
    
    def actualizar_proyecto(self, proyecto):
        self.repository.actualizar(proyecto)
        
    def eliminar_proyecto(self, proyecto_id):
        self.repository.eliminar(proyecto_id)