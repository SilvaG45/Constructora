# Importar la clase de la entidad Subcontratista
from domain.entities.subcontratista import Subcontratista
# Importar el DTO (opcional)
from application.dtos.subcontratista_dto import SubcontratistaDTO


class SubcontratistaMapper:
    @staticmethod
    def to_dict(subcontratista):
        """Convierte un objeto Subcontratista en un diccionario."""
        return {
            "id": subcontratista.id,
            "nombre": subcontratista.nombre,
            "especialidad": subcontratista.especialidad,
            "disponible": subcontratista.disponible,
            "proyectos": subcontratista.proyectos
        }

    @staticmethod
    def from_dict(data):
        """Crea un objeto Subcontratista a partir de un diccionario."""
        return Subcontratista(
            id=data["id"],
            nombre=data["nombre"],
            especialidad=data["especialidad"],
            disponible=data.get("disponible", True)
        )

    @staticmethod
    def to_dto(subcontratista):
        """Convierte un objeto Subcontratista en un DTO."""
        return SubcontratistaDTO(
            id=subcontratista.id,
            nombre=subcontratista.nombre,
            especialidad=subcontratista.especialidad,
            disponible=subcontratista.disponible,
            proyectos=subcontratista.proyectos
        )
