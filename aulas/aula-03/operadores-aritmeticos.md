# Aula 07 - Operadores Aritméticos

## Objetivo da aula

Aprender a realizar operações matemáticas em Python utilizando os operadores aritméticos.

---

## Operadores Aritméticos

### Soma (`+`)

Realiza a soma entre dois valores.

```python
print(5 + 2)
```

Resultado:

```
7
```

---

### Subtração (`-`)

Realiza a diferença entre dois valores.

```python
print(5 - 2)
```

Resultado:

```
3
```

---

### Multiplicação (`*`)

Multiplica dois valores.

```python
print(5 * 2)
```

Resultado:

```
10
```

---

### Divisão (`/`)

Realiza uma divisão e sempre retorna um número decimal (`float`).

```python
print(5 / 2)
```

Resultado:

```
2.5
```

---

### Divisão Inteira (`//`)

Retorna apenas a parte inteira da divisão.

```python
print(5 // 2)
```

Resultado:

```
2
```

---

### Resto da Divisão (`%`)

Retorna o resto da divisão.

```python
print(5 % 2)
```

Resultado:

```
1
```

---

### Potência (`**`)

Eleva um número a outro.

```python
print(5 ** 2)
```

Resultado:

```
25
```

---

## Ordem de Precedência

O Python segue uma ordem para realizar os cálculos.

1. `()`
2. `**`
3. `*`, `/`, `//`, `%`
4. `+` e `-`

### Exemplo

```python
print(5 + 2 * 3)
```

Resultado:

```
11
```

Porque a multiplicação é feita antes da soma.

---

## Formatação de Strings

Podemos utilizar o método `.format()` para inserir valores em uma string.

### Exemplo

```python
nome = "Wallyston"
print("Prazer em te conhecer, {}!".format(nome))
```

---

## O que aprendi

- Como realizar operações matemáticas em Python.
- A diferença entre divisão (`/`) e divisão inteira (`//`).
- Como utilizar o operador de potência (`**`).
- Como descobrir o resto de uma divisão utilizando `%`.
- A importância da ordem de precedência das operações.
- Como utilizar `.format()` para exibir informações.

---

## Aplicação no HotelHub

Os operadores aritméticos serão utilizados para calcular:

- Valor total da hospedagem.
- Quantidade de diárias.
- Descontos.
- Acréscimos.
- Faturamento mensal.
- Média de ocupação dos quartos.

### Exemplo

```python
diaria = 250.00
dias = 4

total = diaria * dias

print("Valor total: R${:.2f}".format(total))
```

Resultado:

```
Valor total: R$1000.00
```