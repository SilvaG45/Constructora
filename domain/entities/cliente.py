class Cliente:
    def __init__(self, id, nombre, direccion, contacto, proyectos=None):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.contacto = contacto
        self.proyectos = proyectos if proyectos else []

    # def coincide_con(self, infoCliente):
    #     """Verifica que la información del cliente sea la misma que los atributos."""
    #     return (
    #         infoCliente.get("nombre") == self.nombre or
    #         infoCliente.get("direccion") == self.direccion or
    #         infoCliente.get("contacto") == self.contacto
    #     )
    # 
    # def agregar_cliente(self, infoCliente):
    #     """Agrega un cliente."""
    #     if "nombre" in infoCliente and "direccion" in infoCliente and "contacto" in infoCliente:
    #         self.nombre = infoCliente["nombre"]
    #         self.direccion = infoCliente["direccion"]
    #         self.contacto = infoCliente["contacto"]
    #         return True
    #     return False
    # 
    # def obtener_proyectos(self):
    #     """Devuelve una lista de proyectos asociados al cliente."""
    #     return self.proyectos