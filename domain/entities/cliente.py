class Cliente:
    def __init__(self, id, nombre, direccion, contacto, proyectos=None):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.contacto = contacto
        self.proyectos = proyectos if proyectos else []