# Módulo: Calculadora Simples
# Descrição: Funções matemáticas básicas com validação de entrada

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


def subtrair(numero1, numero2):
    """Subtrai o segundo número do primeiro."""
    if not isinstance(numero1, (int, float)) or not isinstance(numero2, (int, float)):
        raise TypeError("Os argumentos devem ser números")
    
    return numero1 - numero2


def multiplicar(numero1, numero2):
    """Multiplica dois números."""
    if not isinstance(numero1, (int, float)) or not isinstance(numero2, (int, float)):
        raise TypeError("Os argumentos devem ser números")
    
    return numero1 * numero2


def dividir(numero1, numero2):
    """
    Divide o primeiro número pelo segundo.
    
    Raises:
        ValueError: Se tentar dividir por zero
    """
    if not isinstance(numero1, (int, float)) or not isinstance(numero2, (int, float)):
        raise TypeError("Os argumentos devem ser números")
    
    if numero2 == 0:
        raise ValueError("Não é possível dividir por zero")
    
    return numero1 / numero2