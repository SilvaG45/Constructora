from datetime import date
class Pedido:
    def __init__(self, fecha_pedido=None, id=None):
        self.id = id
        self.fecha_pedido = fecha_pedido or date.today()
        self.materiales_suministrados = []

    def registrar_pedido(self, material, cantidad):
        """Registra un material en el pedido con la cantidad deseada."""
        if material not in self.materiales_suministrados:
            self.materiales_suministrados.append(material)

    def consultar_materiales(self):
        """Devuelve una lista de materiales incluidos en el pedido."""
        return self.materiales_suministrados

    def consultar_historial_pedidos(self, session):
        """Devuelve el historial de pedidos almacenados en la base de datos."""
        return session.query(Pedido).all()