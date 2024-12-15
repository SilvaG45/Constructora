from domain.entities.personal import Personal  # Importa la entidad
from application.dtos.personal_dto import PersonalDTO  # Importa el DTO (opcional)


class PersonalMapper:
    @staticmethod
    def to_dict(personal):
        """Convierte un objeto Personal en un diccionario."""
        return {
            "id": personal.id,
            "nombre": personal.nombre,
            "rol": personal.rol,
            "horas_trabajadas": personal.horas_trabajadas,
            "proyectos": personal.proyectos
        }

    @staticmethod
    def from_dict(data):
        """Crea un objeto Personal a partir de un diccionario."""
        return Personal(
            id=data["id"],
            nombre=data["nombre"],
            rol=data["rol"],
            horas_trabajadas=data.get("horas_trabajadas", 0)
        )

    @staticmethod
    def to_dto(personal):
        """Convierte un objeto Personal en un DTO."""
        return PersonalDTO(
            id=personal.id,
            nombre=personal.nombre,
            rol=personal.rol,
            horas_trabajadas=personal.horas_trabajadas,
            proyectos=personal.proyectos
        )
