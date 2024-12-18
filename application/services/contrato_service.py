from domain.repositories.i_contrato_repository import IContratoRepository
from infrastructure.repositories.sqlite_contrato_repository import SQLiteContratoRepository
from infrastructure.repositories.sqlite_proyecto_repository import SQLiteProyectoRepository
from infrastructure.repositories.sqlite_cliente_repository import SQLiteClienteRepository
from icecream import ic

class ContratoService:
    def __init__(self):
        self.repository = SQLiteContratoRepository()
        self.proyecto_repository = SQLiteProyectoRepository()
        self.cliente_repository = SQLiteClienteRepository()

    def registrar_contrato(self, contrato):
        print(contrato)
        self.repository.agregar(contrato)

    def obtener_contrato(self, contrato_id):
        return self.repository.obtener_por_id(contrato_id)
    
    def obtener_proyecto(self, proyecto_id):
        return self.proyecto_repository.obtener_por_id(proyecto_id)
    
    def obtener_cliente(self, cliente_id):
        return self.cliente_repository.obtener_por_id(cliente_id)
    
    def listar_todos(self):
        return self.repository.listar_todos()
    
    def registrar_contrato_info(self, info_contrato, cliente):
        self.repository.registrarContrato(info_contrato, cliente)

    def actualizar_estado_contrato(self, contrato_id, estado):
        self.repository.actualizarEstado(contrato_id, estado)