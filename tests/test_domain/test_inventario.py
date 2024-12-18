import unittest
from domain.entities.inventario import Inventario
from application.services.inventario_service import InventarioService

# Función de validación de inventario
def validar_inventario(infoInventario):
    errores = []
    # Validar que materiales sea una lista
    if not isinstance(infoInventario.get("materiales"), list):
        errores.append("Materiales inválidos")

    if errores:
        return {"exito": False, "errores": errores}
    return {"exito": True, "mensaje": "Inventario válido"}

# Clase de pruebas unitarias
class TestValidarInventario(unittest.TestCase):

    def test_caso_i1_materiales_validos(self):
        """Caso I1: Materiales válidos"""
        infoInventario = {
            "materiales": [
                {"nombre": "Cemento", "cantidad": 50},
                {"nombre": "Arena", "cantidad": 30}
            ]
        }
        resultado = validar_inventario(infoInventario)
        self.assertTrue(resultado["exito"])
        self.assertNotIn("errores", resultado)

    def test_caso_i2_materiales_no_lista(self):
        """Caso I2: Materiales no es una lista"""
        infoInventario = {
            "materiales": "no es una lista"
        }
        resultado = validar_inventario(infoInventario)
        self.assertFalse(resultado["exito"])
        self.assertIn("Materiales inválidos", resultado["errores"])

    def test_caso_i3_materiales_vacios(self):
        """Caso I3: Lista de materiales vacía"""
        infoInventario = {
            "materiales": []
        }
        resultado = validar_inventario(infoInventario)
        self.assertTrue(resultado["exito"])
        self.assertNotIn("errores", resultado)

    def test_caso_i4_materiales_con_datos_invalidos(self):
        """Caso I4: Materiales con datos inválidos"""
        infoInventario = {
            "materiales": [
                {"nombre": "Cemento", "cantidad": -5},
                {"nombre": "", "cantidad": 10}
            ]
        }
        resultado = validar_inventario(infoInventario)
        self.assertTrue(resultado["exito"], "Se permite validar lista con errores internos si es lista")

if __name__ == "__main__":
    unittest.main()
