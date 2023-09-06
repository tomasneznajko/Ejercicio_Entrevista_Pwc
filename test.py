import unittest
from unittest.mock import patch
from respuesta import *  # Importa las funciones que deseas probar

class TestFunciones(unittest.TestCase):

    def setUp(self):
        self.listaIDs =  [
            {
                "codigoId": "00000",
                "dueDate": "9-08-2023",
                "estado": "Finalizado",
                "cartasFaltantes": True,
                "cartasFirmadas": True,
                "cantidadCambioDueDate": 1,
            },
            {
                "codigoId": "00001",
                "dueDate": "12-09-2023",
                "estado": "En Progreso",
                "cartasFaltantes": True,
                "cartasFirmadas": False,
                "cantidadCambioDueDate": 0,
            },
            {
                "codigoId": "00002",
                "dueDate": "9-05-2023",
                "estado": "Finalizado",
                "cartasFaltantes": False,
                "cartasFirmadas": False,
                "cantidadCambioDueDate": 2,
            },
            {
                "codigoId": "00003",
                "dueDate": "9-11-2023",
                "estado": "En Progreso",
                "cartasFaltantes": False,
                "cartasFirmadas": True,
                "cantidadCambioDueDate": 3,
            }
        ]

    def test_filtrarElementosSegun(self):
        listaFiltrada = filtrarElementosSegun("cartasFirmadas", False, self.listaIDs)
        self.assertEqual(len(listaFiltrada), 2)  # Debería haber 2 elementos sin cartas firmadas

    def test_filtrarIDsFinalizadas(self):
        listaIDs,lista_filtrada = filtrarIDsFinalizadas(self.listaIDs)

                # Verifica que la lista original no contiene elementos con estado "Finalizado"
        for elemento in self.listaIDs:
            self.assertNotEqual(elemento["estado"], "Finalizado")
        
        # Verifica que todos los elementos en lista_filtrada tengan estado "Finalizado"
        for elemento in lista_filtrada:
            self.assertEqual(elemento["estado"], "Finalizado")

if __name__ == '__main__':
    unittest.main()