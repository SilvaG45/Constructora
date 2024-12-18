import unittest
from domain.entities.proveedor import Proveedor
from application.services.proveedor_service import ProveedorService

# Función de validación para proveedores
def validar_proveedor(nombre):
    errores = []
    # Validar nombre del proveedor
    if not nombre or len(nombre) < 3:
        errores.append("Nombre de proveedor inválido")
    if errores:
        return {"exito": False, "errores": errores}
    return {"exito": True, "mensaje": "Proveedor válido"}

# Clase de pruebas unitarias
class TestProveedorService(unittest.TestCase):

    def setUp(self):
        """Configura el servicio antes de cada prueba"""
        self.servicio = ProveedorService()
        self.proveedor_valido = Proveedor("Proveedor Test")
        self.servicio.registrar_proveedor(self.proveedor_valido)

    def test_caso_c1_proveedor_valido(self):
        """Caso C1: Registrar proveedor válido"""
        resultado = validar_proveedor(self.proveedor_valido.nombre)
        self.assertTrue(resultado["exito"])
        self.assertNotIn("errores", resultado)

    def test_caso_c2_nombre_proveedor_vacio(self):
        """Caso C2: Nombre del proveedor vacío"""
        proveedor_invalido = Proveedor("")
        resultado = validar_proveedor(proveedor_invalido.nombre)
        self.assertFalse(resultado["exito"])
        self.assertIn("Nombre de proveedor inválido", resultado["errores"])

    def test_caso_c3_nombre_proveedor_corto(self):
        """Caso C3: Nombre del proveedor demasiado corto"""
        proveedor_invalido = Proveedor("A")
        resultado = validar_proveedor(proveedor_invalido.nombre)
        self.assertFalse(resultado["exito"])
        self.assertIn("Nombre de proveedor inválido", resultado["errores"])

    def test_caso_c4_registrar_pedido_con_proveedor_existente(self):
        """Caso C4: Registrar un pedido para un proveedor existente"""
        proveedor = self.proveedor_valido
        pedido = {"id": 1, "producto": "Material 1", "cantidad": 10}
        proveedor = self.servicio.registrar_pedido(proveedor.id, pedido)
        self.assertIsNotNone(proveedor)
        self.assertIn(pedido, proveedor.historial_pedidos)

    def test_caso_c5_registrar_pedido_con_proveedor_inexistente(self):
        """Caso C5: Registrar un pedido para un proveedor inexistente"""
        proveedor_id_invalido = 9999  # Suponiendo que este id no existe
        pedido = {"id": 1, "producto": "Material 1", "cantidad": 10}
        proveedor = self.servicio.registrar_pedido(proveedor_id_invalido, pedido)
        self.assertIsNone(proveedor)

    def test_caso_c6_obtener_historial_pedidos_con_proveedor_existente(self):
        """Caso C6: Obtener historial de pedidos de un proveedor existente"""
        proveedor = self.proveedor_valido
        pedido = {"id": 1, "producto": "Material 1", "cantidad": 10}
        self.servicio.registrar_pedido(proveedor.id, pedido)
        historial = self.servicio.obtener_historial_pedidos(proveedor.id)
        self.assertIn(pedido, historial)

    def test_caso_c7_obtener_historial_pedidos_con_proveedor_inexistente(self):
        """Caso C7: Obtener historial de pedidos de un proveedor inexistente"""
        proveedor_id_invalido = 9999  # Suponiendo que este id no existe
        historial = self.servicio.obtener_historial_pedidos(proveedor_id_invalido)
        self.assertIsNone(historial)

if __name__ == "__main__":
    unittest.main()
