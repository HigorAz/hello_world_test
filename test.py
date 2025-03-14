import unittest
from script import *

class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world_pt(), 'Olá, Mundo!')
        self.assertEqual(hello_world_en(), 'Hello, World!')
        self.assertEqual(hello_world_ru(), 'Привет, мир!')
        self.assertEqual(hello_world_es(), '¡Hola Mundo!')

if __name__ == "__main__":
    unittest.main()