import unittest
from hello import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_portuguese(self):
        self.assertEqual(hello_world("pt"), "Olá, Mundo!")

    def test_hello_world_english(self):
        self.assertEqual(hello_world("en"), "Hello, World!")

    def test_hello_world_spanish(self):
        self.assertEqual(hello_world("es"), "¡Hola, Mundo!")

    def test_hello_world_russian(self):
        self.assertEqual(hello_world("ru"), "Привет, мир!")


if __name__ == "__main__":
    unittest.main()
