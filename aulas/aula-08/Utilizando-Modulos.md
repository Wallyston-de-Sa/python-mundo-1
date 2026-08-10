# Curso de Python - Mundo 1
## Aula 08 - Utilizando Módulos

Nesta aula aprendi como utilizar **módulos** no Python.

Módulos são recursos que já existem no Python e possuem funções prontas que podemos utilizar em nossos programas.

Isso facilita o desenvolvimento, pois não precisamos criar determinadas funções do zero.

---

## Importando módulos

Podemos importar um módulo inteiro utilizando:

```python
import math
```

Depois podemos acessar uma função desse módulo:

```python
math.sqrt(25)
```

Também podemos importar somente uma função específica:

```python
from math import sqrt

print(sqrt(25))
```

---

# Módulo `math`

O módulo `math` possui várias funções matemáticas.

## `sqrt()`

Calcula a raiz quadrada.

```python
from math import sqrt

num = 25

print(sqrt(num))
```

Resultado:

```text
5.0
```

---

## `ceil()`

Arredonda um número para cima.

```python
from math import ceil

num = 5.2

print(ceil(num))
```

Resultado:

```text
6
```

---

## `floor()`

Arredonda um número para baixo.

```python
from math import floor

num = 5.8

print(floor(num))
```

Resultado:

```text
5
```

---

## `trunc()`

Remove a parte decimal do número.

```python
from math import trunc

num = 5.8

print(trunc(num))
```

Resultado:

```text
5
```

---

## `pow()`

Pode ser utilizado para calcular uma potência.

```python
from math import pow

print(pow(2, 3))
```

Resultado:

```text
8.0
```

Também podemos utilizar o operador `**`:

```python
print(2 ** 3)
```

---

## `hypot()`

Calcula a hipotenusa de um triângulo retângulo.

```python
from math import hypot

oposto = 3
adjacente = 4

print(hypot(oposto, adjacente))
```

Resultado:

```text
5.0
```

---

# Seno, Cosseno e Tangente

O módulo `math` também possui funções para trabalhar com:

- `sin()` → seno
- `cos()` → cosseno
- `tan()` → tangente

Para trabalhar com ângulos em graus, podemos utilizar `radians()` para converter o valor para radianos.

```python
from math import radians, sin, cos, tan

angulo = 30

print(sin(radians(angulo)))
print(cos(radians(angulo)))
print(tan(radians(angulo)))
```

---

# Módulo `random`

Também conheci o módulo `random`.

Ele permite trabalhar com valores aleatórios.

Para importar:

```python
import random
```

---

## `randint()`

Gera um número inteiro aleatório dentro de um intervalo.

```python
import random

num = random.randint(1, 10)

print(num)
```

O resultado pode ser qualquer número entre `1` e `10`.

---

## `shuffle()`

Embaralha os elementos de uma lista.

```python
import random

lista = ['Ana', 'João', 'Maria', 'Pedro']

random.shuffle(lista)

print(lista)
```

A ordem dos elementos será alterada aleatoriamente.

### Uma coisa importante que aprendi

O `shuffle()` modifica a própria lista.

Por isso, não devo fazer:

```python
nova_lista = random.shuffle(lista)
```

Isso não funciona como esperado porque `shuffle()` não retorna uma nova lista.

O correto é:

```python
random.shuffle(lista)
```

Depois podemos utilizar a própria `lista`.

---

## `sample()`

Permite selecionar elementos aleatoriamente de uma lista.

```python
import random

lista = ['Ana', 'João', 'Maria', 'Pedro']

resultado = random.sample(lista, k=2)

print(resultado)
```

Nesse exemplo, serão escolhidos 2 elementos da lista.

---

# O que aprendi nesta aula

Nesta aula entendi que o Python possui vários módulos com funções prontas.

Em vez de criar tudo do zero, podemos importar esses recursos e utilizá-los em nossos programas.

Algumas funções que aprendi:

| Função | Para que serve |
|---|---|
| `sqrt()` | Calcula a raiz quadrada |
| `ceil()` | Arredonda para cima |
| `floor()` | Arredonda para baixo |
| `trunc()` | Remove a parte decimal |
| `pow()` | Calcula potência |
| `hypot()` | Calcula a hipotenusa |
| `sin()` | Calcula seno |
| `cos()` | Calcula cosseno |
| `tan()` | Calcula tangente |
| `randint()` | Gera número aleatório |
| `shuffle()` | Embaralha uma lista |
| `sample()` | Seleciona elementos aleatoriamente |

---

# Aplicando no HotelHub

Consegui utilizar o conteúdo desta aula no projeto **HotelHub**.

Na Missão 004, utilizei:

```python
from math import hypot
```

para calcular a diagonal de um quarto.

Também utilizei:

```python
area = largura * comprimento
```

para calcular a área do quarto.

O código da missão ficou:

```python
from math import hypot

quarto = int(input('Quarto: '))
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))

area = largura * comprimento
diagonal = hypot(largura, comprimento)

print('========= HOTELHUB =========')
print('Quarto: Suite {}'.format(quarto))
print('Largura: {} m'.format(largura))
print('Comprimento: {} m'.format(comprimento))
print('\nÁrea do quarto: {} m²'.format(area))
print('Diagonal do quarto: {:.2f} m'.format(diagonal))
print('=' * 28)
```
```python
import math
```

Nesse caso, preciso indicar o módulo:

```python
math.sqrt(25)
```

Ou posso importar somente a função:

```python
from math import sqrt
```

E utilizar diretamente:

```python
sqrt(25)
```

---

# 🏨 Relação com o HotelHub

O conteúdo desta aula pode ser muito útil no HotelHub.

Alguns exemplos de aplicações futuras:

- Cálculos de áreas dos quartos
- Cálculos de medidas
- Valores e arredondamentos
- Sorteios de quartos
- Seleção aleatória de informações
- Organização de listas
- Outros cálculos utilizados na administração da pousada

A ideia é continuar utilizando o que aprendo no curso para desenvolver o HotelHub aos poucos.

---