class Constructora:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.proyectos = []
        self.inventarios = []
        self.personal = []
        self.subcontratistas = []
        self.proveedores = []
        self.contratos = []
        self.clientes = []

    # def registrar_proyecto(self, info_proyecto, info_contrato, info_cliente) -> None:
    #     proyecto = Proyecto(**info_proyecto)
    #     contrato = Contrato(**info_contrato)
    #     cliente = Cliente(**info_cliente)
    #     proyecto.asignar_contrato(contrato)
    #     proyecto.asignar_cliente(cliente)
    #     self.agregar_proyecto_a_la_lista(proyecto)
    #     self.agregar_contrato_a_la_lista(contrato)
    #     self.clientes.append(cliente)

    # def registrar_contrato(self, info_contrato, info_cliente) -> None:
    #     contrato = Contrato(**info_contrato)
    #     cliente = Cliente(**info_cliente)
    #     self.agregar_contrato_a_la_lista(contrato)
    #     self.clientes.append(cliente)

    # def actualizar_detalles_proyecto(self, proyecto_id: int, nuevo_presupuesto: float, nuevas_fechas) -> None:
    #     proyecto = self.obtener_proyecto(proyecto_id)
    #     if proyecto:
    #         proyecto.actualizar_detalles(nuevo_presupuesto, nuevas_fechas)

    # def buscar_cliente(self, info_cliente) -> 'Cliente':
    #     for cliente in self.clientes:
    #         if cliente.matches(info_cliente):
    #             return cliente
    #     return None

    # def obtener_cliente_existente(self, info_cliente) -> 'Cliente':
    #     cliente = self.buscar_cliente(info_cliente)
    #     if cliente:
    #         return cliente
    #     nuevo_cliente = Cliente(**info_cliente)
    #     self.clientes.append(nuevo_cliente)
    #     return nuevo_cliente

    # def agregar_proyecto_a_la_lista(self, proyecto) -> None:
    #     self.proyectos.append(proyecto)

    # def agregar_contrato_a_la_lista(self, contrato) -> None:
    #     self.contratos.append(contrato)

    # def obtener_proyecto(self, proyecto_id: int) -> 'Proyecto':
    #     for proyecto in self.proyectos:
    #         if proyecto.id == proyecto_id:
    #             return proyecto
    #     return None

    # def registrar_personal(self, info_personal) -> None:
    #     personal = Personal(**info_personal)
    #     self.empleados.append(personal)

    # def registrar_subcontratista(self, info_subcontratista) -> None:
    #     subcontratista = Subcontratista(**info_subcontratista)
    #     self.subcontratistas.append(subcontratista)

    # def registrar_proveedor(self, info_proveedor) -> None:
    #     proveedor = Proveedor(**info_proveedor)
    #     self.proveedores.append(proveedor)

    # def gestionar_inventario(self, nombre_material: str, cantidad: int) -> None:
    #     for inventario in self.inventarios:
    #         if inventario.nombre_material == nombre_material:
    #             inventario.cantidad += cantidad
    #             return
    #     nuevo_inventario = Inventario(nombre_material, cantidad)
    #     self.inventarios.append(nuevo_inventario)