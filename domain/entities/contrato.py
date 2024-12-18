class Contrato:
    def __init__(self, monto, condiciones, estado):
        self.id = None
        self.monto = monto
        self.condiciones = condiciones
        self.estado = estado
        self.cliente = None
        self.proyecto = None 