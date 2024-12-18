import unittest
from domain.entities.subcontratista import Subcontratista
from application.services.subcontratista_service import SubcontratistaService

# Función de validación de subcontratista
def validar_subcontratista(infoSubcontratista):
    errores = []
    # Validar nombre
    if not (isinstance(infoSubcontratista.get("nombre"), str) and len(infoSubcontratista["nombre"]) > 0):
        errores.append("Nombre inválido")
    # Validar especialidad
    if not (isinstance(infoSubcontratista.get("especialidad"), str) and len(infoSubcontratista["especialidad"]) > 0):
        errores.append("Especialidad inválida")
    # Validar disponibilidad
    if not isinstance(infoSubcontratista.get("disponible"), bool):
        errores.append("Disponibilidad inválida")

    if errores:
        return {"exito": False, "errores": errores}
    return {"exito": True, "mensaje": "Subcontratista válido"}

# Clase de pruebas unitarias
class TestValidarSubcontratista(unittest.TestCase):

    def test_caso_s1_todos_validos(self):
        """Caso S1: Todos los datos válidos"""
        infoSubcontratista = {
            "nombre": "Carlos Ramirez",
            "especialidad": "Electricista",
            "disponible": True
        }
        resultado = validar_subcontratista(infoSubcontratista)
        self.assertTrue(resultado["exito"])
        self.assertNotIn("errores", resultado)

    def test_caso_s2_nombre_vacio(self):
        """Caso S2: Nombre vacío"""
        infoSubcontratista = {
            "nombre": "",
            "especialidad": "Electricista",
            "disponible": True
        }
        resultado = validar_subcontratista(infoSubcontratista)
        self.assertFalse(resultado["exito"])
        self.assertIn("Nombre inválido", resultado["errores"])

    def test_caso_s3_especialidad_vacia(self):
        """Caso S3: Especialidad vacía"""
        infoSubcontratista = {
            "nombre": "Carlos Ramirez",
            "especialidad": "",
            "disponible": True
        }
        resultado = validar_subcontratista(infoSubcontratista)
        self.assertFalse(resultado["exito"])
        self.assertIn("Especialidad inválida", resultado["errores"])

    def test_caso_s4_disponibilidad_invalida(self):
        """Caso S4: Disponibilidad inválida"""
        infoSubcontratista = {
            "nombre": "Carlos Ramirez",
            "especialidad": "Electricista",
            "disponible": "si"
        }
        resultado = validar_subcontratista(infoSubcontratista)
        self.assertFalse(resultado["exito"])
        self.assertIn("Disponibilidad inválida", resultado["errores"])

    def test_caso_s5_todos_invalidos(self):
        """Caso S5: Todos los datos inválidos"""
        infoSubcontratista = {
            "nombre": "",
            "especialidad": "",
            "disponible": "si"
        }
        resultado = validar_subcontratista(infoSubcontratista)
        self.assertFalse(resultado["exito"])
        self.assertIn("Nombre inválido", resultado["errores"])
        self.assertIn("Especialidad inválida", resultado["errores"])
        self.assertIn("Disponibilidad inválida", resultado["errores"])

if __name__ == "__main__":
    unittest.main()
