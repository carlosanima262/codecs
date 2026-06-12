# Módulo: Relatório de Cobertura
# Descrição: Gera relatório simples dos testes executados

import unittest
from io import StringIO
import sys


def executar_testes_com_relatorio():
    """Executa testes e gera relatório de resultado"""
    
    # Carrega os testes
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='test_*.py')
    
    # Executa os testes com verbose
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    resultado = runner.run(suite)
    
    # Imprime relatório
    print("=" * 60)
    print("📊 RELATÓRIO DE TESTES DE QUALIDADE DE CÓDIGO")
    print("=" * 60)
    print(stream.getvalue())
    
    # Estatísticas
    total_testes = resultado.testsRun
    falhas = len(resultado.failures)
    erros = len(resultado.errors)
    sucesso = total_testes - falhas - erros
    
    print("\n" + "=" * 60)
    print("📈 RESUMO")
    print("=" * 60)
    print(f"Total de testes executados: {total_testes}")
    print(f"✅ Sucessos: {sucesso}")
    print(f"❌ Falhas: {falhas}")
    print(f"⚠️  Erros: {erros}")
    
    # Percentual de sucesso
    percentual = (sucesso / total_testes * 100) if total_testes > 0 else 0
    print(f"🎯 Cobertura de sucesso: {percentual:.1f}%")
    print("=" * 60)


if __name__ == '__main__':
    executar_testes_com_relatorio()