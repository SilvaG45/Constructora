from datetime import date
class Pedido:
    def __init__(self, numero_pedido, fecha_pedido=None):
        self.numero_pedido = numero_pedido
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