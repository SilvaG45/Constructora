from domain.repositories.i_proveedor_repository import IProveedorRepository
from infrastructure.repositories.sqlite_proveedor_repository import SQLiteProveedorRepository

class ProveedorService:
    def __init__(self):
        self.repository = SQLiteProveedorRepository()

    def registrar_proveedor(self, proveedor):
        self.repository.agregar(proveedor)

    def obtener_proveedor(self, proveedor_id):
        return self.repository.obtener_por_id(proveedor_id)

    def listar_todos(self):
        return self.repository.listar_todos()

    def registrar_pedido(self, proveedor_id, pedido):
        proveedor = self.obtener_proveedor(proveedor_id)
        if proveedor:
            proveedor.registrar_pedido(pedido)
            self.repository.actualizar(proveedor)
            return proveedor
        return None

    def obtener_historial_pedidos(self, proveedor_id):
        proveedor = self.obtener_proveedor(proveedor_id)
        if proveedor:
            return proveedor.obtener_historial_pedidos()
        return None