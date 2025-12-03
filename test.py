import unittest

# Função simples que soma dois números
def somar(a, b):
    return a + b

# Teste unitário
class TestSomar(unittest.TestCase):
    def test_somar(self):
        resultado = somar(2, 3)
        self.assertEqual(resultado, 5)  # Verifica se 2 + 3 = 5

if __name__ == "__main__":
    unittest.main()
