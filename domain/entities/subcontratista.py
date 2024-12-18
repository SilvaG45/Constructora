class Subcontratista:
    def __init__(self, nombre, especialidad, disponible=True, proyectos=None):
        self.id = None
        self.nombre = nombre
        self.especialidad = especialidad
        self.disponible = disponible
        self.proyectos = proyectos if proyectos is not None else []  # Inicializa si no se pasa


    def verificarDisponibilidad(self):
        """Verifica si el subcontratista está disponible para un nuevo proyecto."""
        return self.disponible

    def asignarAProyecto(self, proyecto):
        """Asigna este subcontratista a un proyecto."""
        if self.verificarDisponibilidad():
            self.proyectos.append(proyecto)
            self.disponible = False  # Asumimos que ya no está disponible una vez asignado
            return True
        return False

    def obtenerProyectosAsignados(self):
        """Devuelve la lista de proyectos asignados."""
        return self.proyectos

    def liberarDeProyecto(self, proyecto):
        """Libera al subcontratista de un proyecto, marcándolo como disponible."""
        if proyecto in self.proyectos:
            self.proyectos.remove(proyecto)
            self.disponible = True
            return True
        return False
