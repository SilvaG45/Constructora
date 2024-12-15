class Personal:
    def __init__(self, id, nombre, rol, horas_trabajadas=0):
        self.id = id
        self.nombre = nombre
        self.rol = rol
        self.horas_trabajadas = horas_trabajadas
        self.proyectos = []  # Lista de proyectos asignados

    def registrarHoras(self, horas):
        """Registra las horas trabajadas por el personal."""
        self.horas_trabajadas += horas

    def asignarAProyecto(self, proyecto):
        """Asigna este personal a un proyecto."""
        self.proyectos.append(proyecto)

    def obtenerHorasTrabajadas(self):
        """Devuelve las horas trabajadas totales."""
        return self.horas_trabajadas

    def obtenerProyectosAsignados(self):
        """Devuelve la lista de proyectos asignados."""
        return self.proyectos
