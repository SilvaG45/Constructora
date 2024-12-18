import unittest
from domain.entities.proyecto import Proyecto
from application.services.proyecto_service import ProyectoService

# Función de validación de proyecto
def validar_proyecto(infoProyecto):
    errores = []
    # Validar nombre
    if not (isinstance(infoProyecto.get("nombre"), str) and len(infoProyecto["nombre"]) > 0):
        errores.append("Nombre inválido")
    # Validar presupuesto inicial
    if not (isinstance(infoProyecto.get("presupuesto_inicial"), (int, float)) and infoProyecto["presupuesto_inicial"] > 0):
        errores.append("Presupuesto inicial inválido")
    # Validar fecha de inicio
    if not (isinstance(infoProyecto.get("fecha_inicio"), str) and len(infoProyecto["fecha_inicio"]) > 0):
        errores.append("Fecha de inicio inválida")
    # Validar fecha estimada de fin
    if not (isinstance(infoProyecto.get("fecha_estimacion_fin"), str) and len(infoProyecto["fecha_estimacion_fin"]) > 0):
        errores.append("Fecha estimada de fin inválida")

    if errores:
        return {"exito": False, "errores": errores}
    return {"exito": True, "mensaje": "Proyecto válido"}

# Clase de pruebas unitarias
class TestValidarProyecto(unittest.TestCase):

    def test_caso_pr1_todos_validos(self):
        """Caso PR1: Todos los datos válidos"""
        infoProyecto = {
            "nombre": "Construcción de Puente",
            "presupuesto_inicial": 500000.0,
            "fecha_inicio": "2024-01-01",
            "fecha_estimacion_fin": "2024-12-31"
        }
        resultado = validar_proyecto(infoProyecto)
        self.assertTrue(resultado["exito"])
        self.assertNotIn("errores", resultado)

    def test_caso_pr2_nombre_vacio(self):
        """Caso PR2: Nombre vacío"""
        infoProyecto = {
            "nombre": "",
            "presupuesto_inicial": 500000.0,
            "fecha_inicio": "2024-01-01",
            "fecha_estimacion_fin": "2024-12-31"
        }
        resultado = validar_proyecto(infoProyecto)
        self.assertFalse(resultado["exito"])
        self.assertIn("Nombre inválido", resultado["errores"])

    def test_caso_pr3_presupuesto_negativo(self):
        """Caso PR3: Presupuesto inicial negativo"""
        infoProyecto = {
            "nombre": "Construcción de Puente",
            "presupuesto_inicial": -1000.0,
            "fecha_inicio": "2024-01-01",
            "fecha_estimacion_fin": "2024-12-31"
        }
        resultado = validar_proyecto(infoProyecto)
        self.assertFalse(resultado["exito"])
        self.assertIn("Presupuesto inicial inválido", resultado["errores"])

    def test_caso_pr4_fecha_inicio_vacia(self):
        """Caso PR4: Fecha de inicio vacía"""
        infoProyecto = {
            "nombre": "Construcción de Puente",
            "presupuesto_inicial": 500000.0,
            "fecha_inicio": "",
            "fecha_estimacion_fin": "2024-12-31"
        }
        resultado = validar_proyecto(infoProyecto)
        self.assertFalse(resultado["exito"])
        self.assertIn("Fecha de inicio inválida", resultado["errores"])

    def test_caso_pr5_fecha_estimacion_fin_vacia(self):
        """Caso PR5: Fecha estimada de fin vacía"""
        infoProyecto = {
            "nombre": "Construcción de Puente",
            "presupuesto_inicial": 500000.0,
            "fecha_inicio": "2024-01-01",
            "fecha_estimacion_fin": ""
        }
        resultado = validar_proyecto(infoProyecto)
        self.assertFalse(resultado["exito"])
        self.assertIn("Fecha estimada de fin inválida", resultado["errores"])

    def test_caso_pr6_todos_invalidos(self):
        """Caso PR6: Todos los datos inválidos"""
        infoProyecto = {
            "nombre": "",
            "presupuesto_inicial": -1000.0,
            "fecha_inicio": "",
            "fecha_estimacion_fin": ""
        }
        resultado = validar_proyecto(infoProyecto)
        self.assertFalse(resultado["exito"])
        self.assertIn("Nombre inválido", resultado["errores"])
        self.assertIn("Presupuesto inicial inválido", resultado["errores"])
        self.assertIn("Fecha de inicio inválida", resultado["errores"])
        self.assertIn("Fecha estimada de fin inválida", resultado["errores"])

if __name__ == "__main__":
    unittest.main()
