import domain.entities.pedido as Pedido
class Proveedor:    
    def __init__(self, nombre):
        self.nombre = nombre
        self.materiales_suministrados = []
        self.historial_pedidos = []

    def registrar_pedido(self, material, cantidad):
        """Registra un nuevo pedido para el proveedor."""
        nuevo_pedido = Pedido(proveedor=self, material=material, cantidad=cantidad)
        self.historial_pedidos.append(nuevo_pedido)

    def consultar_historial_pedidos(self):
        """Devuelve una lista con el historial de pedidos del proveedor."""
        return self.historial_pedidos

    def actualizar_material_suministrado(self, material):
        """Agrega un material suministrado si no está ya en la lista."""
        if material not in self.materiales_suministrados:
            self.materiales_suministrados.append(material)