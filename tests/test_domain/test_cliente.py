import unittest
from domain.entities.cliente import Cliente
from application.services.cliente_service import ClienteService

# Función de validación de cliente
def validar_cliente(infoCliente):
    errores = []
    # Validar nombre
    if not (isinstance(infoCliente.get("nombre"), str) and len(infoCliente["nombre"]) > 0):
        errores.append("Nombre inválido")
    # Validar dirección
    if not (isinstance(infoCliente.get("direccion"), str) and len(infoCliente["direccion"]) > 0):
        errores.append("Dirección inválida")
    # Validar contacto
    if not (isinstance(infoCliente.get("contacto"), str) and len(infoCliente["contacto"]) > 0):
        errores.append("Contacto inválido")

    if errores:
        return {"exito": False, "errores": errores}
    return {"exito": True, "mensaje": "Cliente válido"}

# Clase de pruebas unitarias
class TestValidarCliente(unittest.TestCase):

    def test_caso_c1_todos_validos(self):
        """Caso C1: Todos los datos válidos"""
        infoCliente = {
            "nombre": "Juan Perez",
            "direccion": "Calle Falsa 123",
            "contacto": "1234567890"
        }
        resultado = validar_cliente(infoCliente)
        self.assertTrue(resultado["exito"])
        self.assertNotIn("errores", resultado)

    def test_caso_c2_nombre_vacio(self):
        """Caso C2: Nombre vacío"""
        infoCliente = {
            "nombre": "",
            "direccion": "Calle Falsa 123",
            "contacto": "1234567890"
        }
        resultado = validar_cliente(infoCliente)
        self.assertFalse(resultado["exito"])
        self.assertIn("Nombre inválido", resultado["errores"])

    def test_caso_c3_direccion_vacia(self):
        """Caso C3: Dirección vacía"""
        infoCliente = {
            "nombre": "Juan Perez",
            "direccion": "",
            "contacto": "1234567890"
        }
        resultado = validar_cliente(infoCliente)
        self.assertFalse(resultado["exito"])
        self.assertIn("Dirección inválida", resultado["errores"])

    def test_caso_c4_contacto_vacio(self):
        """Caso C4: Contacto vacío"""
        infoCliente = {
            "nombre": "Juan Perez",
            "direccion": "Calle Falsa 123",
            "contacto": ""
        }
        resultado = validar_cliente(infoCliente)
        self.assertFalse(resultado["exito"])
        self.assertIn("Contacto inválido", resultado["errores"])

    def test_caso_c5_todos_invalidos(self):
        """Caso C5: Todos los datos inválidos"""
        infoCliente = {
            "nombre": "",
            "direccion": "",
            "contacto": ""
        }
        resultado = validar_cliente(infoCliente)
        self.assertFalse(resultado["exito"])
        self.assertIn("Nombre inválido", resultado["errores"])
        self.assertIn("Dirección inválida", resultado["errores"])
        self.assertIn("Contacto inválido", resultado["errores"])

if __name__ == "__main__":
    unittest.main()
