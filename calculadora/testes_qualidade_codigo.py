"""
CALCULADORA SIMPLES COM TESTES
"""

import unittest
from io import StringIO


class Calculadora:
    """Operações matemáticas básicas"""
    
    @staticmethod
    def somar(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Argumentos devem ser números")
        return a + b
    
    @staticmethod
    def subtrair(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Argumentos devem ser números")
        return a - b
    
    @staticmethod
    def multiplicar(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Argumentos devem ser números")
        return a * b
    
    @staticmethod
    def dividir(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Argumentos devem ser números")
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b


class TestCalculadora(unittest.TestCase):
    """Testes da Calculadora"""
    
    def setUp(self):
        self.calc = Calculadora()
    
    def test_somar(self):
        self.assertEqual(self.calc.somar(2, 3), 5)
    
    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(5, 3), 2)
    
    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(4, 5), 20)
    
    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
    
    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)
    
    def test_tipo_invalido(self):
        with self.assertRaises(TypeError):
            self.calc.somar("5", 3)


def main():
    calc = Calculadora()
    
    print("=" * 40)
    print("🧮 CALCULADORA")
    print("=" * 40)
    
    while True:
        try:
            print("\n1. Somar  2. Subtrair  3. Multiplicar  4. Dividir  5. Testes  6. Sair")
            opcao = input("Opção: ").strip()
            
            if opcao == "6":
                print("Até logo!\n")
                break
            
            if opcao == "5":
                loader = unittest.TestLoader()
                suite = loader.loadTestsFromTestCase(TestCalculadora)
                runner = unittest.TextTestRunner(verbosity=2)
                runner.run(suite)
                continue
            
            if opcao not in ["1", "2", "3", "4"]:
                print("Opção inválida!")
                continue
            
            a = float(input("Primeiro número: "))
            b = float(input("Segundo número: "))
            
            if opcao == "1":
                resultado = calc.somar(a, b)
                print(f"Resultado: {a} + {b} = {resultado}")
            elif opcao == "2":
                resultado = calc.subtrair(a, b)
                print(f"Resultado: {a} - {b} = {resultado}")
            elif opcao == "3":
                resultado = calc.multiplicar(a, b)
                print(f"Resultado: {a} × {b} = {resultado}")
            elif opcao == "4":
                resultado = calc.dividir(a, b)
                print(f"Resultado: {a} ÷ {b} = {resultado}")
        
        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro: {e}")


if __name__ == '__main__':
    main()
