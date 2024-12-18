import unittest
from domain.entities.contrato import Contrato
from application.services.contrato_service import ContratoService

# Función de validación de contrato
def validar_contrato(infoContrato):
    errores = []
    # Validar monto
    if not (isinstance(infoContrato.get("monto"), (int, float)) and infoContrato["monto"] > 0):
        errores.append("Monto inválido")
    # Validar condiciones
    if not (isinstance(infoContrato.get("condiciones"), str) and len(infoContrato["condiciones"]) > 0):
        errores.append("Condiciones inválidas")
    # Validar estado
    if not (infoContrato.get("estado") in ["pendiente", "activo", "finalizado"]):
        errores.append("Estado inválido")

    if errores:
        return {"exito": False, "errores": errores}
    return {"exito": True, "mensaje": "Contrato válido"}

# Clase de pruebas unitarias
class TestValidarContrato(unittest.TestCase):

    def test_caso_c1_todos_validos(self):
        """Caso C1: Todos los datos válidos"""
        infoContrato = {
            "monto": 10000.50,
            "condiciones": "Pago en dos partes",
            "estado": "pendiente"
        }
        resultado = validar_contrato(infoContrato)
        self.assertTrue(resultado["exito"])
        self.assertNotIn("errores", resultado)

    def test_caso_c2_monto_negativo(self):
        """Caso C2: Monto negativo"""
        infoContrato = {
            "monto": -500,
            "condiciones": "Pago en dos partes",
            "estado": "pendiente"
        }
        resultado = validar_contrato(infoContrato)
        self.assertFalse(resultado["exito"])
        self.assertIn("Monto inválido", resultado["errores"])

    def test_caso_c3_condiciones_vacias(self):
        """Caso C3: Condiciones vacías"""
        infoContrato = {
            "monto": 10000.50,
            "condiciones": "",
            "estado": "pendiente"
        }
        resultado = validar_contrato(infoContrato)
        self.assertFalse(resultado["exito"])
        self.assertIn("Condiciones inválidas", resultado["errores"])

    def test_caso_c4_estado_invalido(self):
        """Caso C4: Estado inválido"""
        infoContrato = {
            "monto": 10000.50,
            "condiciones": "Pago en dos partes",
            "estado": "cancelado"
        }
        resultado = validar_contrato(infoContrato)
        self.assertFalse(resultado["exito"])
        self.assertIn("Estado inválido", resultado["errores"])

    def test_caso_c5_todos_invalidos(self):
        """Caso C5: Todos los datos inválidos"""
        infoContrato = {
            "monto": -500,
            "condiciones": "",
            "estado": "cancelado"
        }
        resultado = validar_contrato(infoContrato)
        self.assertFalse(resultado["exito"])
        self.assertIn("Monto inválido", resultado["errores"])
        self.assertIn("Condiciones inválidas", resultado["errores"])
        self.assertIn("Estado inválido", resultado["errores"])

if __name__ == "__main__":
    unittest.main()
