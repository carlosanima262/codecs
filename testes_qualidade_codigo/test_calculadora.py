# Módulo: Testes da Calculadora
# Descrição: Testes unitários para validar qualidade do código

import unittest
from calculadora import somar, subtrair, multiplicar, dividir


class TestCalculadora(unittest.TestCase):
    """Classe de testes para a calculadora"""
    
    # ===== TESTES DA SOMA =====
    def test_somar_inteiros(self):
        """Testa soma de dois inteiros"""
        self.assertEqual(somar(2, 3), 5)
    
    def test_somar_floats(self):
        """Testa soma de números decimais"""
        self.assertAlmostEqual(somar(1.5, 2.3), 3.8)
    
    def test_somar_negativos(self):
        """Testa soma com números negativos"""
        self.assertEqual(somar(-5, 3), -2)
    
    def test_somar_tipo_invalido(self):
        """Testa soma com tipo inválido - deve gerar erro"""
        with self.assertRaises(TypeError):
            somar("5", 3)
    
    # ===== TESTES DA SUBTRAÇÃO =====
    def test_subtrair_inteiros(self):
        """Testa subtração de inteiros"""
        self.assertEqual(subtrair(5, 3), 2)
    
    def test_subtrair_resultado_negativo(self):
        """Testa subtração com resultado negativo"""
        self.assertEqual(subtrair(3, 5), -2)
    
    # ===== TESTES DA MULTIPLICAÇÃO =====
    def test_multiplicar_inteiros(self):
        """Testa multiplicação de inteiros"""
        self.assertEqual(multiplicar(4, 5), 20)
    
    def test_multiplicar_por_zero(self):
        """Testa multiplicação por zero"""
        self.assertEqual(multiplicar(100, 0), 0)
    
    # ===== TESTES DA DIVISÃO =====
    def test_dividir_inteiros(self):
        """Testa divisão de inteiros"""
        self.assertEqual(dividir(10, 2), 5)
    
    def test_dividir_por_zero(self):
        """Testa divisão por zero - deve gerar erro"""
        with self.assertRaises(ValueError):
            dividir(10, 0)
    
    def test_dividir_resultado_decimal(self):
        """Testa divisão com resultado decimal"""
        self.assertAlmostEqual(dividir(7, 2), 3.5)


if __name__ == '__main__':
    unittest.main()