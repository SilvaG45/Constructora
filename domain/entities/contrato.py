class Contrato:
    def __init__(self, monto, condiciones, estado, cliente=None, proyecto= None,id=None):
        self.id = id
        self.monto = monto
        self.condiciones = condiciones
        self.estado = estado
        self.cliente = cliente
        self.proyecto = proyecto 
        
    def __str__(self):
        id_str = f"{self.id} - " if self.id is not None else ""
        return f"{id_str}{self.monto} - {self.condiciones} - {self.estado} - {self.cliente} - {self.proyecto}"