from datetime import date
class Pedido:
    def __init__(self, fecha_pedido=None, id=None, proveedor_id=None):
        self.id = id
        self.fecha_pedido = fecha_pedido or date.today()
        self.materiales_suministrados = []
        self.proveedor_id = proveedor_id
    
        
    def __str__(self):
        return f"{self.fecha_pedido} - {self.materiales_suministrados}"