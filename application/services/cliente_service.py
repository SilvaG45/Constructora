from domain.repositories.i_cliente_repository import IClienteRepository
from infrastructure.repositories.sqlite_cliente_repository import SQLiteClienteRepository
from domain.entities.cliente import Cliente

class ClienteService:
    def __init__ (self):
        self.repository = SQLiteClienteRepository()
    
    def registrar_cliente(self, cliente):
        self.repository.agregar(cliente)

    def obtener_cliente(self, cliente_id):
        return self.repository.obtener_por_id(cliente_id)
    
    def listar_todos(self):
        return self.repository.listar_todos()
    
    def coincide_con(self, infoCliente):
        return self.repository.coincide_con(infoCliente)
    
    def agregar_cliente(self, infoCliente):
        cliente = Cliente(
            id=infoCliente["id"],  
            nombre=infoCliente["nombre"],
            direccion=infoCliente["direccion"],
            contacto=infoCliente["contacto"],
            proyectos=infoCliente.get("proyectos", [])
        )
        self.repository.agregar(cliente)

    def obtener_proyectos(self, cliente_id):
        cliente = self.repository.obtener_por_id(cliente_id)
        return cliente.proyectos if cliente else []
    
    