import unittest
from domain.entities.material import Material
from application.services.material_service import MaterialService

# Función de validación de material
def validar_material(infoMaterial):
    errores = []
    # Validar que el nombre sea una cadena no vacía
    if not isinstance(infoMaterial.get("nombre"), str) or not infoMaterial["nombre"].strip():
        errores.append("Nombre inválido")
    
    # Validar que la cantidad disponible sea un entero no negativo
    if not isinstance(infoMaterial.get("cantidad_disponible"), int) or infoMaterial["cantidad_disponible"] < 0:
        errores.append("Cantidad disponible inválida")

    # Validar que el precio sea un número positivo
    if not isinstance(infoMaterial.get("precio"), (int, float)) or infoMaterial["precio"] <= 0:
        errores.append("Precio inválido")

    if errores:
        return {"exito": False, "errores": errores}
    return {"exito": True, "mensaje": "Material válido"}

# Clase de pruebas unitarias
class TestValidarMaterial(unittest.TestCase):

    def test_caso_m1_material_valido(self):
        """Caso M1: Material válido"""
        infoMaterial = {
            "nombre": "Cemento",
            "cantidad_disponible": 50,
            "precio": 100.0
        }
        resultado = validar_material(infoMaterial)
        self.assertTrue(resultado["exito"])
        self.assertNotIn("errores", resultado)

    def test_caso_m2_nombre_invalido(self):
        """Caso M2: Nombre inválido"""
        infoMaterial = {
            "nombre": "",
            "cantidad_disponible": 50,
            "precio": 100.0
        }
        resultado = validar_material(infoMaterial)
        self.assertFalse(resultado["exito"])
        self.assertIn("Nombre inválido", resultado["errores"])

    def test_caso_m3_cantidad_disponible_invalida(self):
        """Caso M3: Cantidad disponible inválida"""
        infoMaterial = {
            "nombre": "Arena",
            "cantidad_disponible": -10,
            "precio": 50.0
        }
        resultado = validar_material(infoMaterial)
        self.assertFalse(resultado["exito"])
        self.assertIn("Cantidad disponible inválida", resultado["errores"])

    def test_caso_m4_precio_invalido(self):
        """Caso M4: Precio inválido"""
        infoMaterial = {
            "nombre": "Grava",
            "cantidad_disponible": 20,
            "precio": -15.0
        }
        resultado = validar_material(infoMaterial)
        self.assertFalse(resultado["exito"])
        self.assertIn("Precio inválido", resultado["errores"])

    def test_caso_m5_todos_los_datos_invalidos(self):
        """Caso M5: Todos los datos inválidos"""
        infoMaterial = {
            "nombre": "",
            "cantidad_disponible": -5,
            "precio": 0
        }
        resultado = validar_material(infoMaterial)
        self.assertFalse(resultado["exito"])
        self.assertIn("Nombre inválido", resultado["errores"])
        self.assertIn("Cantidad disponible inválida", resultado["errores"])
        self.assertIn("Precio inválido", resultado["errores"])

if __name__ == "__main__":
    unittest.main()
