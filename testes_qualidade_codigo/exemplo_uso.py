# Módulo: Exemplo de Uso
# Descrição: Demonstra como usar a calculadora com boas práticas

from calculadora import somar, subtrair, multiplicar, dividir


def main():
    """Função principal com exemplos de uso"""
    
    print("🧮 DEMONSTRAÇÃO DE CALCULADORA COM TESTES DE QUALIDADE")
    print("-" * 50)
    
    # Exemplo 1: Soma
    try:
        resultado = somar(10, 5)
        print(f"✓ Soma: 10 + 5 = {resultado}")
    except Exception as erro:
        print(f"✗ Erro na soma: {erro}")
    
    # Exemplo 2: Subtração
    try:
        resultado = subtrair(10, 3)
        print(f"✓ Subtração: 10 - 3 = {resultado}")
    except Exception as erro:
        print(f"✗ Erro na subtração: {erro}")
    
    # Exemplo 3: Multiplicação
    try:
        resultado = multiplicar(7, 8)
        print(f"✓ Multiplicação: 7 × 8 = {resultado}")
    except Exception as erro:
        print(f"✗ Erro na multiplicação: {erro}")
    
    # Exemplo 4: Divisão (sucesso)
    try:
        resultado = dividir(20, 4)
        print(f"✓ Divisão: 20 ÷ 4 = {resultado}")
    except Exception as erro:
        print(f"✗ Erro na divisão: {erro}")
    
    # Exemplo 5: Divisão por zero (erro esperado)
    try:
        resultado = dividir(10, 0)
        print(f"✓ Divisão: 10 ÷ 0 = {resultado}")
    except ValueError as erro:
        print(f"✗ Erro esperado: {erro}")
    
    # Exemplo 6: Tipo inválido (erro esperado)
    try:
        resultado = somar("10", 5)
        print(f"✓ Soma: '10' + 5 = {resultado}")
    except TypeError as erro:
        print(f"✗ Erro esperado: {erro}")
    
    print("-" * 50)


if __name__ == '__main__':
    main()