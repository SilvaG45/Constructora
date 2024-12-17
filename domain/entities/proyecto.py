class Proyecto:
    def __init__(self, nombre, presupuesto_inicial, fecha_inicio, fecha_estimacion_fin, porcentaje_avance=0.0):
        self.nombre = nombre
        self.presupuesto_inicial = presupuesto_inicial
        self.fecha_inicio = fecha_inicio
        self.fecha_estimacion_fin = fecha_estimacion_fin
        self.porcentaje_avance = porcentaje_avance
        self.contrato = None  # Ningún contrato asignado inicialmente
        self.materiales = {}  # Diccionario vacío para materiales
        self.personal_asignado = {}  # Diccionario vacío para personal
        self.subcontratistas = {}  # Diccionario vacío para subcontratistas
        
    # def actualizar_detalles(self, presupuesto, fecha):
    #     self.presupuesto_inicial = presupuesto
    #     self.fecha_estimacion_fin = fecha

    # def verificar_avance(self):
    #     return self.porcentaje_avance

    # def asignar_personal(self, personal):
    #     self.personal_asignado.append(personal)

    # def asignar_subcontratista(self, subcontratista):
    #     self.subcontratistas.append(subcontratista)

    # def consultar_materiales_necesarios(self):
    #     return self.materiales

    # def asignar_contrato(self, contrato):
    #     self.contrato = contrato
    
    def __str__(self):
        return f"{self.nombre} - {self.presupuesto_inicial} - {self.fecha_inicio} - {self.fecha_estimacion_fin} - {self.porcentaje_avance}"