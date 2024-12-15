from domain.repositories.i_cliente_repository import IClienteRepository
from infrastructure.repositories.sqlite_cliente_repository import SQLiteClienteRepository

class ClienteService:
    def __init__ (self):
        self.repository = SQLiteClienteRepository()
    
    def registrar_cliente(self, cliente):
        self.repository.agregar(cliente)

    def obtener_cliente(self, cliente_id):
        return self.repository.obtener_por_id(cliente_id)
    
    def listar_todos(self):
        return self.repository.listar_todos()