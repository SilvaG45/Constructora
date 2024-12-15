import unittest
import sqlite3
from domain.entities.subcontratista import Subcontratista
from infrastructure.repositories.sqlite_subcontratista_repository import SQLiteSubcontratistaRepository

class TestSQLiteSubcontratistaRepository(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.repo = SQLiteSubcontratistaRepository()
        self.repo.conn = self.conn
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE subcontratistas (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            especialidad TEXT NOT NULL,
            disponible BOOLEAN DEFAULT 1
        )
        """)
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_agregar_subcontratista(self):
        subcontratista = Subcontratista(1, "Carlos Gutiérrez", "Carpintero", True)
        self.repo.agregar(subcontratista)
        result = self.repo.obtener_por_id(1)
        self.assertIsNotNone(result)
        self.assertEqual(result.nombre, "Carlos Gutiérrez")

    def test_listar_subcontratistas(self):
        self.repo.agregar(Subcontratista(1, "Juan Pérez", "Electricista", True))
        self.repo.agregar(Subcontratista(2, "María Gómez", "Plomera", False))
        subcontratistas = self.repo.listar_todos()
        self.assertEqual(len(subcontratistas), 2)

if __name__ == "__main__":
    unittest.main()
