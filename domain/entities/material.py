class Material:
    def __init__(self, nombre, cantidad_disponible, precio):
            self.nombre = nombre
            self.cantidad_disponible = cantidad_disponible
            self.precio = precio

    def consultar_disponibilidad(self):
        """Devuelve True si hay cantidad disponible, False de lo contrario."""
        return self.cantidad_disponible > 0

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio del material."""
        if nuevo_precio > 0:
            self.precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser un valor positivo.")