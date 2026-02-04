from datetime import datetime, date
from os import name
import unittest

def sum(a,b):
    if not isinstance(a, (int, float)) or not isinstance (b, (int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales")
    return a + b

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(2,8), 10)
        self.assertEqual(sum(2,9), 12)
        self.assertEqual(sum(2,3), 5)

        with self.assertRaises(ValueError):
            sum("5", 7)
        with self.assertRaises(ValueError):
            sum(5, "7")
        with self.assertRaises(ValueError):
            sum("5", "7")
        with self.assertRaises(ValueError):
            sum("a", 7)
        with self.assertRaises(ValueError):
            sum(None, 7) 

# Se usa para ejecutar todos los def que empiece por "test_" y debe de estar en un class para poder ejecutar

unittest.main()

# EXTRA



class test_campos(unittest.TestCase):

    def setUp(self) -> None:
            self.diccionario = {
                "name": "Andres Franco",
                "age": 17,
                "birthday": datetime.strptime("26-07-08", "%d-%m-%y").date(),
                "lenguages": ["Python", "Html", "C#"]
            }

# self.assertIn es para comprobar si algo existe dentro de algo

    def test_existen(self):
        self.assertIn("name", self.diccionario)
        self.assertIn("age", self.diccionario)
        self.assertIn("birthday", self.diccionario)
        self.assertIn("lenguages", self.diccionario)

        # if len(self.diccionario)>0:
        #     print("Haz ingresado correctamente todos los datos")
        # else:
        #     print("No has ingresado correctamente todos los datos")
    
    def test_correct(self):
        self.assertIsInstance(self.diccionario["name"], str)
        self.assertIsInstance(self.diccionario["age"], int)
        self.assertIsInstance(self.diccionario["birthday"], date)
        self.assertIsInstance(self.diccionario["lenguages"], list)

unittest.main()