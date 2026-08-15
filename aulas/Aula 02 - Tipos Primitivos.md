# Aula 02 - Tipos Primitivos e Saída de Dados

## Objetivo da aula

Aprender os principais tipos primitivos do Python e como utilizá-los em conjunto com o comando `input()`.

---

## Tipos Primitivos

### `int`

Representa números inteiros.

**Exemplos:**

```python
idade = 23
ano = 2026
```

---

### `float`

Representa números reais (com casas decimais).

**Exemplos:**

```python
altura = 1.65
preco = 19.90
```

---

### `bool`

Representa valores lógicos.

Possui apenas dois valores:

- `True`
- `False`

**Exemplos:**

```python
aprovado = True
ligado = False
```

---

### `str`

Representa textos (strings).

**Exemplos:**

```python
nome = "Wallyston"
cidade = "Pirenópolis"
```

---

## O comando `type()`

A função `type()` permite identificar o tipo de uma variável.

**Exemplo:**

```python
nome = "Wallyston"
print(type(nome))
```

**Saída:**

```python
<class 'str'>
```

---

## Convertendo tipos

Como o `input()` sempre retorna uma **string**, é necessário converter quando desejamos trabalhar com números.

**Exemplos:**

```python
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
```

---

## O que aprendi

- Existem diferentes tipos primitivos em Python.
- O `input()` sempre retorna uma `str`.
- Podemos converter valores utilizando funções como `int()` e `float()`.
- A função `type()` informa o tipo de uma variável.

---

## Aplicação no HotelHub

Ao cadastrar um hóspede, alguns dados precisarão ser convertidos para o tipo correto.

Exemplo:

- Nome → `str`
- Idade → `int`
- Valor da diária → `float`
- Hóspede VIP → `bool`

Utilizar os tipos corretos facilita os cálculos e evita erros no sistema.