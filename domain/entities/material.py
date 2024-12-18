class Material:
    def __init__(self, nombre, precio, id=None):
            self.id = id
            self.nombre = nombre
            self.precio = precio

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio del material."""
        if nuevo_precio > 0:
            self.precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser un valor positivo.")
        
    def __str__(self):
        id_str = f"{self.id} - " if self.id is not None else ""
        return f"{id_str}{self.nombre} - {self.precio}"