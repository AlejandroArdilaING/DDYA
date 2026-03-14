import unittest

class TestProcesarEstudiantes(unittest.TestCase):

    def test_caso_mixto(self):
        entrada = ["Ana", 4.5, "Luis", 2.8, "Marta", 3.0]
        resultados, aprobados = procesar_estudiantes(entrada)
        self.assertEqual(resultados, {
            "Ana": "aprobado",
            "Luis": "reprobado",
            "Marta": "aprobado"
        })
        self.assertEqual(aprobados, ["Ana", "Marta"])

    def test_todos_aprobados(self):
        entrada = ["Carlos", 5.0, "Sofía", 4.2]
        resultados, aprobados = procesar_estudiantes(entrada)
        self.assertEqual(len(aprobados), 2)

    def test_todos_reprobados(self):
        entrada = ["Pedro", 1.5, "Laura", 2.9]
        resultados, aprobados = procesar_estudiantes(entrada)
        self.assertEqual(aprobados, [])

    def test_nota_limite(self):
        entrada = ["Diego", 3.0]
        resultados, aprobados = procesar_estudiantes(entrada)
        self.assertEqual(resultados["Diego"], "aprobado")

    def test_lista_vacia(self):
        entrada = []
        resultados, aprobados = procesar_estudiantes(entrada)
        self.assertEqual(resultados, {})
        self.assertEqual(aprobados, [])

    def test_un_reprobado(self):
        entrada = ["Lucía", 2.5]
        resultados, aprobados = procesar_estudiantes(entrada)
        self.assertEqual(resultados["Lucía"], "reprobado")

    def test_nombre_repetido(self):
        entrada = ["Ana", 4.0, "Ana", 2.0]
        resultados, aprobados = procesar_estudiantes(entrada)
        self.assertEqual(resultados["Ana"], "reprobado")

    def test_nota_alta(self):
        entrada = ["Mateo", 10.0]
        resultados, aprobados = procesar_estudiantes(entrada)
        self.assertTrue("Mateo" in aprobados)

    def test_nota_negativa(self):
        entrada = ["Sara", -1.0]
        resultados, aprobados = procesar_estudiantes(entrada)
        self.assertEqual(aprobados, [])

    def test_varios_estudiantes(self):
        entrada = ["A",3.0,"B",3.1,"C",2.9,"D",5.0,"E",1.0]
        resultados, aprobados = procesar_estudiantes(entrada)
        self.assertEqual(aprobados, ["A","B","D"])


if __name__ == "__main__":
    unittest.main()
