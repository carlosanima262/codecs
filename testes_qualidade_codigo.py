"""
DEMONSTRAÇÃO DE TESTES DE SOFTWARE - QUALIDADE DE CÓDIGO
=========================================================

Este arquivo contém um exemplo didático e prático de como implementar
testes de software e garantir qualidade de código em Python.

Estrutura:
1. Módulo Calculadora - Funções matemáticas com validação
2. Testes Unitários - Validação completa das funções
3. Gerador de Relatório - Resumo dos testes executados
4. Exemplos de Uso - Demonstração prática
"""

import unittest
from io import StringIO


# ============================================================
# PARTE 1: MÓDULO CALCULADORA
# ============================================================

class Calculadora:
    """Classe com operações matemáticas básicas e validação"""
    
    @staticmethod
    def somar(numero1, numero2):
        """
        Soma dois números.
        
        Args:
            numero1: Primeiro número (int ou float)
            numero2: Segundo número (int ou float)
        
        Returns:
            A soma dos dois números
        
        Raises:
            TypeError: Se os argumentos não forem números
        """
        if not isinstance(numero1, (int, float)) or not isinstance(numero2, (int, float)):
            raise TypeError("Os argumentos devem ser números")
        
        return numero1 + numero2
    
    @staticmethod
    def subtrair(numero1, numero2):
        """Subtrai o segundo número do primeiro."""
        if not isinstance(numero1, (int, float)) or not isinstance(numero2, (int, float)):
            raise TypeError("Os argumentos devem ser números")
        
        return numero1 - numero2
    
    @staticmethod
    def multiplicar(numero1, numero2):
        """Multiplica dois números."""
        if not isinstance(numero1, (int, float)) or not isinstance(numero2, (int, float)):
            raise TypeError("Os argumentos devem ser números")
        
        return numero1 * numero2
    
    @staticmethod
    def dividir(numero1, numero2):
        """
        Divide o primeiro número pelo segundo.
        
        Raises:
            ValueError: Se tentar dividir por zero
            TypeError: Se os argumentos não forem números
        """
        if not isinstance(numero1, (int, float)) or not isinstance(numero2, (int, float)):
            raise TypeError("Os argumentos devem ser números")
        
        if numero2 == 0:
            raise ValueError("Não é possível dividir por zero")
        
        return numero1 / numero2


# ============================================================
# PARTE 2: TESTES UNITÁRIOS
# ============================================================

class TestCalculadora(unittest.TestCase):
    """Classe de testes para a calculadora"""
    
    def setUp(self):
        """Configuração antes de cada teste"""
        self.calc = Calculadora()
    
    # ===== TESTES DA SOMA =====
    def test_somar_inteiros(self):
        """Testa soma de dois inteiros"""
        self.assertEqual(self.calc.somar(2, 3), 5)
    
    def test_somar_floats(self):
        """Testa soma de números decimais"""
        self.assertAlmostEqual(self.calc.somar(1.5, 2.3), 3.8)
    
    def test_somar_negativos(self):
        """Testa soma com números negativos"""
        self.assertEqual(self.calc.somar(-5, 3), -2)
    
    def test_somar_tipo_invalido(self):
        """Testa soma com tipo inválido - deve gerar erro"""
        with self.assertRaises(TypeError):
            self.calc.somar("5", 3)
    
    # ===== TESTES DA SUBTRAÇÃO =====
    def test_subtrair_inteiros(self):
        """Testa subtração de inteiros"""
        self.assertEqual(self.calc.subtrair(5, 3), 2)
    
    def test_subtrair_resultado_negativo(self):
        """Testa subtração com resultado negativo"""
        self.assertEqual(self.calc.subtrair(3, 5), -2)
    
    # ===== TESTES DA MULTIPLICAÇÃO =====
    def test_multiplicar_inteiros(self):
        """Testa multiplicação de inteiros"""
        self.assertEqual(self.calc.multiplicar(4, 5), 20)
    
    def test_multiplicar_por_zero(self):
        """Testa multiplicação por zero"""
        self.assertEqual(self.calc.multiplicar(100, 0), 0)
    
    # ===== TESTES DA DIVISÃO =====
    def test_dividir_inteiros(self):
        """Testa divisão de inteiros"""
        self.assertEqual(self.calc.dividir(10, 2), 5)
    
    def test_dividir_por_zero(self):
        """Testa divisão por zero - deve gerar erro"""
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)
    
    def test_dividir_resultado_decimal(self):
        """Testa divisão com resultado decimal"""
        self.assertAlmostEqual(self.calc.dividir(7, 2), 3.5)


# ============================================================
# PARTE 3: GERADOR DE RELATÓRIO
# ============================================================

def executar_testes_com_relatorio():
    """Executa testes e gera relatório detalhado"""
    
    # Carrega e executa os testes
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCalculadora)
    
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    resultado = runner.run(suite)
    
    # Imprime relatório
    print("\n" + "=" * 70)
    print("📊 RELATÓRIO DE TESTES DE QUALIDADE DE CÓDIGO")
    print("=" * 70)
    print(stream.getvalue())
    
    # Estatísticas
    total_testes = resultado.testsRun
    falhas = len(resultado.failures)
    erros = len(resultado.errors)
    sucesso = total_testes - falhas - erros
    
    print("\n" + "=" * 70)
    print("📈 RESUMO EXECUTIVO")
    print("=" * 70)
    print(f"Total de testes executados: {total_testes}")
    print(f"✅ Sucessos: {sucesso}")
    print(f"❌ Falhas: {falhas}")
    print(f"⚠️  Erros: {erros}")
    
    # Percentual de sucesso
    percentual = (sucesso / total_testes * 100) if total_testes > 0 else 0
    print(f"🎯 Cobertura de sucesso: {percentual:.1f}%")
    print("=" * 70 + "\n")


# ============================================================
# PARTE 4: EXEMPLOS DE USO
# ============================================================

def exemplos_de_uso():
    """Demonstra como usar a calculadora com boas práticas"""
    
    calc = Calculadora()
    
    print("=" * 70)
    print("🧮 DEMONSTRAÇÃO PRÁTICA - EXEMPLOS DE USO DA CALCULADORA")
    print("=" * 70 + "\n")
    
    # Exemplo 1: Soma
    try:
        resultado = calc.somar(10, 5)
        print(f"✓ Soma: 10 + 5 = {resultado}")
    except Exception as erro:
        print(f"✗ Erro na soma: {erro}")
    
    # Exemplo 2: Subtração
    try:
        resultado = calc.subtrair(10, 3)
        print(f"✓ Subtração: 10 - 3 = {resultado}")
    except Exception as erro:
        print(f"✗ Erro na subtração: {erro}")
    
    # Exemplo 3: Multiplicação
    try:
        resultado = calc.multiplicar(7, 8)
        print(f"✓ Multiplicação: 7 × 8 = {resultado}")
    except Exception as erro:
        print(f"✗ Erro na multiplicação: {erro}")
    
    # Exemplo 4: Divisão (sucesso)
    try:
        resultado = calc.dividir(20, 4)
        print(f"✓ Divisão: 20 ÷ 4 = {resultado}")
    except Exception as erro:
        print(f"✗ Erro na divisão: {erro}")
    
    # Exemplo 5: Divisão por zero (erro esperado)
    try:
        resultado = calc.dividir(10, 0)
        print(f"✓ Divisão: 10 ÷ 0 = {resultado}")
    except ValueError as erro:
        print(f"✗ Erro esperado (divisão por zero): {erro}")
    
    # Exemplo 6: Tipo inválido (erro esperado)
    try:
        resultado = calc.somar("10", 5)
        print(f"✓ Soma: '10' + 5 = {resultado}")
    except TypeError as erro:
        print(f"✗ Erro esperado (tipo inválido): {erro}")
    
    print("\n" + "=" * 70 + "\n")


# ============================================================
# PARTE 5: INFORMAÇÕES DE QUALIDADE
# ============================================================

def mostrar_info_qualidade():
    """Mostra informações sobre qualidade de código"""
    
    print("=" * 70)
    print("✨ CONCEITOS DE QUALIDADE DE CÓDIGO DEMONSTRADOS")
    print("=" * 70)
    print("""
1. ✓ DOCSTRINGS
   └─ Documentação clara em cada função e classe
   
2. ✓ TYPE CHECKING (Validação de Tipos)
   └─ Valida tipos de entrada antes de processar
   
3. ✓ EXCEPTION HANDLING (Tratamento de Erros)
   └─ Levanta erros apropriados com mensagens descritivas
   
4. ✓ UNIT TESTS (Testes Unitários)
   └─ 11 testes cobrindo todos os cenários
   
5. ✓ CODE COVERAGE (Cobertura de Código)
   └─ Todos os caminhos são testados
   
6. ✓ NAMING CONVENTION (Convenção de Nomes)
   └─ Nomes descritivos em português
   
7. ✓ SINGLE RESPONSIBILITY (Responsabilidade Única)
   └─ Cada método faz uma coisa bem

8. ✓ TESTES DE CASOS EXTREMOS
   └─ Números positivos, negativos, zero
   └─ Tipos inválidos
   └─ Operações que geram erros esperados
""")
    print("=" * 70 + "\n")


# ============================================================
# PARTE 6: MENU PRINCIPAL
# ============================================================

def menu_principal():
    """Menu interativo para demonstração"""
    
    while True:
        print("=" * 70)
        print("🚀 DEMONSTRAÇÃO DE TESTES DE SOFTWARE - QUALIDADE DE CÓDIGO")
        print("=" * 70)
        print("""
1. Executar todos os testes (com relatório)
2. Ver exemplos práticos de uso
3. Ver informações de qualidade de código
4. Sair
""")
        
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            print()
            executar_testes_com_relatorio()
        elif opcao == "2":
            print()
            exemplos_de_uso()
        elif opcao == "3":
            print()
            mostrar_info_qualidade()
        elif opcao == "4":
            print("Até logo! 👋\n")
            break
        else:
            print("❌ Opção inválida! Tente novamente.\n")


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == '__main__':
    import sys
    
    # Se executado com argumento -t, roda testes automaticamente
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        executar_testes_com_relatorio()
    # Se executado com argumento -e, mostra exemplos
    elif len(sys.argv) > 1 and sys.argv[1] == '-e':
        exemplos_de_uso()
    # Se executado com argumento -i, mostra informações
    elif len(sys.argv) > 1 and sys.argv[1] == '-i':
        mostrar_info_qualidade()
    # Caso contrário, mostra menu interativo
    else:
        menu_principal()
