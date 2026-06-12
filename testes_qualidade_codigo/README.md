## 📊 Demonstração de Testes de Software - Qualidade de Código

Este diretório contém um exemplo didático e prático de como implementar **testes de software** e garantir a **qualidade de código** em Python.

---

## 📁 Estrutura do Projeto

```
testes_qualidade_codigo/
├── calculadora.py              # Módulo principal com funções matemáticas
├── test_calculadora.py         # Testes unitários
├── relatorio_testes.py         # Gerador de relatório
├── exemplo_uso.py              # Exemplos de uso
└── README.md                   # Este arquivo
```

---

## 🎯 O que é Testado?

A demonstração utiliza uma **Calculadora Simples** com as operações:
- ✅ **Soma** - Adiciona dois números
- ✅ **Subtração** - Subtrai números
- ✅ **Multiplicação** - Multiplica números
- ✅ **Divisão** - Divide números (com validação de divisão por zero)

---

## 🚀 Como Executar

### 1. **Executar Testes Unitários**
```bash
cd testes_qualidade_codigo
python -m unittest test_calculadora.py -v
```

### 2. **Gerar Relatório de Testes**
```bash
python relatorio_testes.py
```

### 3. **Executar Exemplo de Uso**
```bash
python exemplo_uso.py
```

---

## 📈 Conceitos de Qualidade de Código Demonstrados

| Conceito | Descrição | Arquivo |
|----------|-----------|---------|
| **Docstrings** | Documentação clara em cada função | `calculadora.py` |
| **Type Checking** | Validação de tipos de entrada | `calculadora.py` |
| **Exception Handling** | Tratamento de erros apropriados | `calculadora.py` |
| **Unit Tests** | Testes para cada funcionalidade | `test_calculadora.py` |
| **Code Coverage** | Todos os cenários são testados | `test_calculadora.py` |
| **Naming Convention** | Nomes descritivos em português | Todos os arquivos |
| **Single Responsibility** | Cada função faz uma coisa bem | `calculadora.py` |

---

## ✨ Principais Características

### ✓ Validação de Entrada
```python
if not isinstance(numero1, (int, float)):
    raise TypeError("Os argumentos devem ser números")
```

### ✓ Tratamento de Erros
```python
if numero2 == 0:
    raise ValueError("Não é possível dividir por zero")
```

### ✓ Testes Parametrizados
```python
def test_somar_inteiros(self):
    self.assertEqual(somar(2, 3), 5)

def test_somar_tipo_invalido(self):
    with self.assertRaises(TypeError):
        somar("5", 3)
```

### ✓ Testes de Casos Extremos
- Números positivos e negativos
- Valores zero
- Tipos inválidos
- Operações que geram erros esperados

---

## 📊 Saída Esperada

Quando você executa `relatorio_testes.py`, verá:

```
============================================================
📊 RELATÓRIO DE TESTES DE QUALIDADE DE CÓDIGO
============================================================
test_somar_inteiros ... ok
test_somar_floats ... ok
test_subtrair_inteiros ... ok
test_multiplicar_inteiros ... ok
test_dividir_por_zero ... ok
...

============================================================
📈 RESUMO
============================================================
Total de testes executados: 11
✅ Sucessos: 11
❌ Falhas: 0
⚠️  Erros: 0
🎯 Cobertura de sucesso: 100.0%
============================================================
```

---

## 📚 Para Aprender Mais

Este projeto demonstra as melhores práticas de teste:

1. **Testes Positivos** - Verificam se a função funciona corretamente
2. **Testes Negativos** - Verificam se erros são tratados corretamente
3. **Testes Extremos** - Verificam casos limite (zero, negativos, etc.)
4. **Cobertura** - Todos os cenários da função são testados

---

## 💡 Dicas de Qualidade

✅ Escreva testes ANTES de escrever o código (TDD)
✅ Cada teste deve validar UMA coisa
✅ Use nomes descritivos para os testes
✅ Mantenha a cobertura de testes acima de 80%
✅ Documente suas funções com docstrings
✅ Valide tipos e valores de entrada
✅ Trate exceções apropriadamente

---

**Criado para fins didáticos de demonstração de qualidade de código em Python** 🐍
