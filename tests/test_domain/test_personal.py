import unittest
from domain.entities.personal import Personal
from application.services.personal_service import PersonalService

# Función de validación de personal
def validar_personal(infoPersonal):
    errores = []
    # Validar nombre
    if not (isinstance(infoPersonal.get("nombre"), str) and len(infoPersonal["nombre"]) > 0):
        errores.append("Nombre inválido")
    # Validar rol
    if not (isinstance(infoPersonal.get("rol"), str) and len(infoPersonal["rol"]) > 0):
        errores.append("Rol inválido")
    # Validar horas trabajadas
    if not (isinstance(infoPersonal.get("horas_trabajadas"), int) and infoPersonal["horas_trabajadas"] >= 0):
        errores.append("Horas trabajadas inválidas")

    if errores:
        return {"exito": False, "errores": errores}
    return {"exito": True, "mensaje": "Personal válido"}

# Clase de pruebas unitarias
class TestValidarPersonal(unittest.TestCase):

    def test_caso_p1_todos_validos(self):
        """Caso P1: Todos los datos válidos"""
        infoPersonal = {
            "nombre": "Ana Lopez",
            "rol": "Ingeniera",
            "horas_trabajadas": 40
        }
        resultado = validar_personal(infoPersonal)
        self.assertTrue(resultado["exito"])
        self.assertNotIn("errores", resultado)

    def test_caso_p2_nombre_vacio(self):
        """Caso P2: Nombre vacío"""
        infoPersonal = {
            "nombre": "",
            "rol": "Ingeniera",
            "horas_trabajadas": 40
        }
        resultado = validar_personal(infoPersonal)
        self.assertFalse(resultado["exito"])
        self.assertIn("Nombre inválido", resultado["errores"])

    def test_caso_p3_rol_vacio(self):
        """Caso P3: Rol vacío"""
        infoPersonal = {
            "nombre": "Ana Lopez",
            "rol": "",
            "horas_trabajadas": 40
        }
        resultado = validar_personal(infoPersonal)
        self.assertFalse(resultado["exito"])
        self.assertIn("Rol inválido", resultado["errores"])

    def test_caso_p4_horas_negativas(self):
        """Caso P4: Horas trabajadas negativas"""
        infoPersonal = {
            "nombre": "Ana Lopez",
            "rol": "Ingeniera",
            "horas_trabajadas": -5
        }
        resultado = validar_personal(infoPersonal)
        self.assertFalse(resultado["exito"])
        self.assertIn("Horas trabajadas inválidas", resultado["errores"])

    def test_caso_p5_todos_invalidos(self):
        """Caso P5: Todos los datos inválidos"""
        infoPersonal = {
            "nombre": "",
            "rol": "",
            "horas_trabajadas": -5
        }
        resultado = validar_personal(infoPersonal)
        self.assertFalse(resultado["exito"])
        self.assertIn("Nombre inválido", resultado["errores"])
        self.assertIn("Rol inválido", resultado["errores"])
        self.assertIn("Horas trabajadas inválidas", resultado["errores"])

if __name__ == "__main__":
    unittest.main()
