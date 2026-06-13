# 🧮 Calculadora Simples com Testes Unitários

## 📋 Descrição

Este projeto é uma calculadora interativa em Python que demonstra conceitos fundamentais de **testes de software** e **qualidade de código**. O programa permite ao usuário realizar operações matemáticas básicas (soma, subtração, multiplicação e divisão) com validação de entrada e tratamento de erros.

---

## 🎯 Como Funciona

### 1. **Estrutura do Código**

O programa é dividido em 3 partes principais:

#### **Classe Calculadora**
```python
class Calculadora:
    @staticmethod
    def somar(a, b)
    @staticmethod
    def subtrair(a, b)
    @staticmethod
    def multiplicar(a, b)
    @staticmethod
    def dividir(a, b)
```

- Contém 4 métodos estáticos para operações matemáticas
- **Valida tipos**: verifica se os argumentos são números (int ou float)
- **Trata erros**: levanta `TypeError` para tipos inválidos e `ValueError` para divisão por zero

#### **Classe TestCalculadora**
```python
class TestCalculadora(unittest.TestCase)
```

- 6 testes unitários que cobrem todos os cenários
- Testa operações normais
- Testa divisão por zero
- Testa entrada com tipo inválido

#### **Função main()**
- Menu interativo com 6 opções
- Pede entrada do usuário para os números
- Executa a operação escolhida
- Exibe o resultado ou mensagem de erro

---

### 2. **Fluxo de Execução**

```
┌─────────────────────┐
│   INICIA PROGRAMA   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────┐
│  EXIBE MENU COM 6 OPÇÕES    │
│ 1.Somar 2.Subtrair 3.Mult   │
│ 4.Dividir 5.Testes 6.Sair   │
└──────────┬──────────────────┘
           │
      ┌────┴────┬────────┬───────┬─────────┬─────┐
      ▼         ▼        ▼       ▼         ▼     ▼
   SOMA    SUBTRAÇÃO  MULT    DIVISÃO   TESTES SAIR
      │         │        │       │         │     │
      └────┬────┴────┬───┴───┬───┴─────┬──┴─────┴──────┐
           ▼         │       │         │               │
      PEDE 2 NOS    │       │         │               │
           │         │       │         │               │
           ▼         │       │         │               │
      VALIDA TIPO◄───┴───────┘         │               │
           │                           │               │
      SIM │ NÃO                        │               │
      ┌───┘ │                          │               │
      ▼     ▼                          ▼               ▼
   CALCULA  ERRO              EXECUTA TESTES       FINALIZA
      │     │                       │
      └─────┴───────┬────────────────┘
                    ▼
            VOLTA AO MENU OU SAIR
```

---

### 3. **Opções do Menu**

| Opção | Função | O que acontece |
|-------|--------|---|
| **1** | Somar | Pede 2 números e soma |
| **2** | Subtrair | Pede 2 números e subtrai |
| **3** | Multiplicar | Pede 2 números e multiplica |
| **4** | Dividir | Pede 2 números e divide (verifica zero) |
| **5** | Testes | Executa 6 testes unitários |
| **6** | Sair | Finaliza o programa |

---

### 4. **Tratamento de Erros**

O programa detecta e trata 3 tipos de erro:

```python
# ❌ Tipo inválido
>>> calc.somar("5", 3)
TypeError: Argumentos devem ser números

# ❌ Divisão por zero
>>> calc.dividir(10, 0)
ValueError: Não é possível dividir por zero

# ❌ Entrada inválida do usuário
>>> Digite o primeiro número: abc
ValueError (capturado e mostra mensagem)
```

---

### 5. **Testes Unitários (Opção 5)**

Quando você escolhe a opção 5, o programa executa 6 testes automáticos:

```
test_somar ✓          (2 + 3 = 5)
test_subtrair ✓       (5 - 3 = 2)
test_multiplicar ✓    (4 × 5 = 20)
test_dividir ✓        (10 ÷ 2 = 5)
test_dividir_por_zero ✓   (10 ÷ 0 = ValueError)
test_tipo_invalido ✓      ("5" + 3 = TypeError)

Resultado: 6 testes, 6 sucessos ✅
```

---

## 🚀 Como Usar

### 1. **Executar o Programa**

```bash
python testes_qualidade_codigo.py
```

### 2. **Exemplo Prático - Soma**

```
🧮 CALCULADORA
================

1. Somar  2. Subtrair  3. Multiplicar  4. Dividir  5. Testes  6. Sair
Opção: 1
Primeiro número: 10
Segundo número: 5
Resultado: 10.0 + 5.0 = 15.0
```

### 3. **Exemplo Prático - Erro**

```
Opção: 4
Primeiro número: 10
Segundo número: 0
Erro: Não é possível dividir por zero
```

### 4. **Executar Testes**

```
Opção: 5

test_somar ... ok
test_subtrair ... ok
test_multiplicar ... ok
test_dividir ... ok
test_dividir_por_zero ... ok
test_tipo_invalido ... ok

------
Ran 6 tests in 0.001s
OK ✓
```

---

## 📚 Conceitos de Qualidade de Código Implementados

✅ **Documentação** - Docstrings em cada classe e função  
✅ **Validação de Tipos** - Verifica tipos antes de processar  
✅ **Tratamento de Erros** - Try/except para capturar exceções  
✅ **Testes Unitários** - 6 testes cobrindo todos os cenários  
✅ **Nomes Descritivos** - Variáveis e funções com nomes claros  
✅ **Responsabilidade Única** - Cada método faz uma coisa bem  
✅ **Modularização** - Código organizado em funções reutilizáveis  

---

## 🔍 Estrutura de Arquivos

```
calculadora/
│
├── README.md                      # Este arquivo
└── testes_qualidade_codigo.py     # Código da calculadora
```

---

## 💡 Dicas

- Use números inteiros ou decimais (ex: 10, 5.5)
- A divisão sempre retorna um resultado decimal
- Escolha a opção 5 para ver se todos os testes passam
- Escolha a opção 6 para sair do programa

---

## ✨ Resumo

Este projeto é uma **demonstração prática e educacional** de como implementar:
- Uma aplicação com entrada do usuário
- Validação de dados
- Testes unitários
- Tratamento de exceções
- Boas práticas de programação em Python

**Perfeito para aprender sobre qualidade de código!** 🎓
