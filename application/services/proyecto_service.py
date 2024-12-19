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
        
    def asignar_contrato(self, proyecto):
        self.repository.asignar_contrato(proyecto)
        
    def eliminar_proyecto(self, proyecto_id):
        self.repository.eliminar(proyecto_id)
        
    def cambiar_fecha_fin_proyecto(self, proyecto_id, data):
        self.repository.cambiar_fecha_fin(proyecto_id, data)     
    
    def cambiar_presupuesto(self, proyecto_id, data):
        self.repository.cambiar_presupuesto(proyecto_id, data)
        
    def agregar_materiales(self, data):
        return self.repository.agregar_materiales(data)
    
    def verificar_disponibilidad_materiales(self, proyecto_id):
        """Verifica si hay suficiente inventario para los materiales de un proyecto."""
        materiales = self.repository.obtener_materiales_proyecto(proyecto_id)

        for material in materiales:
            material_id, requerida, disponible = material
            if requerida > disponible:
                return False, material_id  # Insuficiente inventario para este material

        return True, None

    def avanzar_proyecto(self, proyecto_id):
        """Verifica la disponibilidad de materiales y permite avanzar el proyecto."""
        disponible, material_insuficiente = self.verificar_disponibilidad_materiales(proyecto_id)

        if not disponible:
            raise ValueError(f"No hay suficiente inventario para el material con ID {material_insuficiente}")

        # Si hay suficiente inventario, descontar los materiales y avanzar el proyecto
        self.proyecto_repositorio.descontar_materiales(proyecto_id)
