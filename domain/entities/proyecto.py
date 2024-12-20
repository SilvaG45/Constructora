class Proyecto:
    def __init__(self, nombre, presupuesto_inicial, fecha_inicio, fecha_estimacion_fin, porcentaje_avance=0.0, id=None):
        self._id = id  # No se asigna un id inicialmente
        self._nombre = nombre
        self._presupuesto_inicial = presupuesto_inicial
        self._fecha_inicio = fecha_inicio
        self._fecha_estimacion_fin = fecha_estimacion_fin
        self._porcentaje_avance = porcentaje_avance
        self._materiales = []  # Diccionario vacío para materiales
        self._personal_asignado = []  # Diccionario vacío para personal
        self._subcontratistas = []  # Diccionario vacío para subcontratistas

    # Getters y Setters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def presupuesto_inicial(self):
        return self._presupuesto_inicial

    @presupuesto_inicial.setter
    def presupuesto_inicial(self, value):
        self._presupuesto_inicial = value

    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value):
        self._fecha_inicio = value

    @property
    def fecha_estimacion_fin(self):
        return self._fecha_estimacion_fin

    @fecha_estimacion_fin.setter
    def fecha_estimacion_fin(self, value):
        self._fecha_estimacion_fin = value

    @property
    def porcentaje_avance(self):
        return self._porcentaje_avance

    @porcentaje_avance.setter
    def porcentaje_avance(self, value):
        self._porcentaje_avance = value

    @property
    def contrato(self):
        return self._contrato
    
    @contrato.setter
    def contrato(self, value):
        self._contrato = value

    @property
    def materiales(self):
        return self._materiales

    @property
    def personal_asignado(self):
        return self._personal_asignado

    @property
    def subcontratistas(self):
        return self._subcontratistas

    # Métodos adicionales

    def agregar_material(self, material_id, cantidad):
        self.materiales[material_id] = cantidad

    def asignar_personal(self, personal_id, horas):
        self.personal_asignado[personal_id] = horas

    def asignar_subcontratista(self, subcontratista_id, especialidad):
        self.subcontratistas[subcontratista_id] = especialidad

    def verificar_avance(self):
        return self.porcentaje_avance

    def __str__(self):
        id_str = f"{self._id} - " if self._id is not None else ""
        return f"{id_str}{self.nombre} - {self.presupuesto_inicial} - {self.fecha_inicio} - {self.fecha_estimacion_fin} - {self.porcentaje_avance}"