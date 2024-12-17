from domain.repositories.i_pedido_repository import IPedidoRepository
from infrastructure.repositories.sqlite_pedido_repository import SQLitePedidoRepository

class PedidoService:
    def __init__(self):
        self.repository = SQLitePedidoRepository()

    def registrar_pedido(self, pedido):
        self.repository.agregar(pedido)

    def obtener_pedido(self, pedido_id):
        return self.repository.obtener_por_id(pedido_id)

    def listar_todos(self):
        return self.repository.listar_todos()

    def agregar_material_a_pedido(self, pedido_id, material_id, cantidad):
        pedido = self.obtener_pedido(pedido_id)
        if pedido:
            pedido.agregar_material(material_id, cantidad)
            self.repository.actualizar(pedido)
            return pedido
        return None

    def consultar_materiales(self, pedido_id):
        return self.repository.consultar_materiales(pedido_id)