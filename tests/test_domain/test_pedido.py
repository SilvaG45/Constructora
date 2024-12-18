import unittest
from domain.entities.pedido import Pedido
from application.services.pedido_service import PedidoService

# Función de validación de pedido
def validar_pedido(infoPedido):
    errores = []
    # Validar que la fecha del pedido sea válida
    if not isinstance(infoPedido.get("fecha_pedido"), str) or not infoPedido["fecha_pedido"].strip():
        errores.append("Fecha de pedido inválida")

    # Validar que los materiales suministrados sean una lista
    if not isinstance(infoPedido.get("materiales_suministrados"), list):
        errores.append("Materiales suministrados inválidos")

    if errores:
        return {"exito": False, "errores": errores}
    return {"exito": True, "mensaje": "Pedido válido"}

# Clase de pruebas unitarias
class TestValidarPedido(unittest.TestCase):

    def test_caso_p1_pedido_valido(self):
        """Caso P1: Pedido válido"""
        infoPedido = {
            "fecha_pedido": "2024-12-18",
            "materiales_suministrados": [
                {"material_id": 1, "cantidad": 10},
                {"material_id": 2, "cantidad": 20}
            ]
        }
        resultado = validar_pedido(infoPedido)
        self.assertTrue(resultado["exito"])
        self.assertNotIn("errores", resultado)

    def test_caso_p2_fecha_invalida(self):
        """Caso P2: Fecha de pedido inválida"""
        infoPedido = {
            "fecha_pedido": "",
            "materiales_suministrados": [
                {"material_id": 1, "cantidad": 10},
                {"material_id": 2, "cantidad": 20}
            ]
        }
        resultado = validar_pedido(infoPedido)
        self.assertFalse(resultado["exito"])
        self.assertIn("Fecha de pedido inválida", resultado["errores"])

    def test_caso_p3_materiales_invalidos(self):
        """Caso P3: Materiales suministrados inválidos"""
        infoPedido = {
            "fecha_pedido": "2024-12-18",
            "materiales_suministrados": "no es una lista"
        }
        resultado = validar_pedido(infoPedido)
        self.assertFalse(resultado["exito"])
        self.assertIn("Materiales suministrados inválidos", resultado["errores"])

    def test_caso_p4_todos_los_datos_invalidos(self):
        """Caso P4: Todos los datos inválidos"""
        infoPedido = {
            "fecha_pedido": "",
            "materiales_suministrados": "no es una lista"
        }
        resultado = validar_pedido(infoPedido)
        self.assertFalse(resultado["exito"])
        self.assertIn("Fecha de pedido inválida", resultado["errores"])
        self.assertIn("Materiales suministrados inválidos", resultado["errores"])

if __name__ == "__main__":
    unittest.main()
