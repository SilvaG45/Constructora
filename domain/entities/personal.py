class Personal:
    def __init__(self, nombre, rol, horas_trabajadas=0, id=None):
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
    
    # set para cambiar las horas trabajadas
    def setHorasTrabajadas(self, horas):
        self.horas_trabajadas = horas
    
    def __str__(self):
        id_str = f"{self.id} - " if self.id is not None else ""
        return f"{id_str}{self.nombre} - {self.rol} - {self.horas_trabajadas}"
