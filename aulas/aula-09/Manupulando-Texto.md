# Curso de Python - Mundo 1
## Aula 09 - Manipulando Texto

Nesta aula aprendi como trabalhar melhor com **strings (textos)** no Python.

Aprendi que uma string pode ser manipulada de várias formas, como:

- Contar caracteres
- Encontrar partes de um texto
- Trocar palavras
- Transformar letras maiúsculas e minúsculas
- Remover espaços
- Separar textos
- Juntar textos

---

# Strings

Uma string é um texto dentro de aspas.

Podemos usar aspas simples:

```python
nome = 'Wallyston'
```

Ou aspas duplas:

```python
nome = "Wallyston"
```

Também podemos trabalhar diretamente com textos:

```python
print('Olá, mundo!')
```

---

# Fatiamento de Strings

Podemos pegar apenas uma parte de uma string utilizando colchetes `[]`.

Por exemplo:

```python
frase = 'Curso de Python'
```

Podemos pegar um caractere específico:

```python
print(frase[0])
```

Resultado:

```text
C
```

Isso acontece porque o Python começa a contar as posições a partir do `0`.

---

## Pegando uma parte do texto

Podemos utilizar:

```python
frase[0:5]
```

Exemplo:

```python
frase = 'Curso de Python'

print(frase[0:5])
```

Resultado:

```text
Curso
```

O último número não é incluído.

---

## Pulando caracteres

Também podemos utilizar um terceiro valor:

```python
frase[0:15:2]
```

Nesse caso, o `2` indica que queremos pular de dois em dois caracteres.

---

# `len()`

A função `len()` mostra quantos caracteres existem em uma string.

```python
frase = 'Curso de Python'

print(len(frase))
```

Resultado:

```text
15
```

Os espaços também são considerados caracteres.

---

# `count()`

O método `count()` conta quantas vezes determinado caractere ou texto aparece.

```python
frase = 'Curso de Python'

print(frase.count('o'))
```

Isso mostra quantas vezes a letra `o` aparece na frase.

Também podemos utilizar com fatiamento:

```python
print(frase.count('o', 0, 10))
```

---

# `find()`

O método `find()` procura uma determinada parte dentro da string.

```python
frase = 'Curso de Python'

print(frase.find('Python'))
```

Ele retorna a posição onde o texto foi encontrado.

Se não encontrar, retorna:

```text
-1
```

---

# `in`

Também podemos verificar se uma palavra existe dentro de uma string utilizando `in`.

```python
frase = 'Curso de Python'

print('Python' in frase)
```

Resultado:

```text
True
```

Se o texto não existir, o resultado será:

```text
False
```

---

# `replace()`

O método `replace()` permite substituir uma parte do texto por outra.

```python
frase = 'Eu estudo Java'

print(frase.replace('Java', 'Python'))
```

Resultado:

```text
Eu estudo Python
```

Isso não altera a string original automaticamente. Para guardar a alteração, podemos fazer:

```python
frase = frase.replace('Java', 'Python')
```

---

# `upper()`

Transforma todas as letras em maiúsculas.

```python
nome = 'Wallyston'

print(nome.upper())
```

Resultado:

```text
WALLYSTON
```

---

# `lower()`

Transforma todas as letras em minúsculas.

```python
nome = 'Wallyston'

print(nome.lower())
```

Resultado:

```text
wallyston
```

---

# `capitalize()`

Deixa a primeira letra da string em maiúscula e o restante em minúsculo.

```python
nome = 'wallyston'

print(nome.capitalize())
```

Resultado:

```text
Wallyston
```

---

# `title()`

Coloca a primeira letra de cada palavra em maiúscula.

```python
frase = 'curso de python'

print(frase.title())
```

Resultado:

```text
Curso De Python
```

---

# `strip()`

Remove espaços desnecessários no começo e no final da string.

```python
nome = '   Wallyston   '

print(nome.strip())
```

Resultado:

```text
Wallyston
```

---

## `lstrip()`

Remove espaços do lado esquerdo.

```python
nome = '   Wallyston'

print(nome.lstrip())
```

---

## `rstrip()`

Remove espaços do lado direito.

```python
nome = 'Wallyston   '

print(nome.rstrip())
```

---

# `split()`

O método `split()` divide uma string em partes e cria uma lista.

```python
frase = 'Curso de Python'

print(frase.split())
```

Resultado:

```text
['Curso', 'de', 'Python']
```

Por padrão, ele utiliza os espaços para separar as palavras.

---

# `join()`

O método `join()` faz o contrário do `split()`.

Ele junta os elementos de uma lista utilizando um separador.

```python
palavras = ['Curso', 'de', 'Python']

frase = ' '.join(palavras)

print(frase)
```

Resultado:

```text
Curso de Python
```

---

# 🧠 O que aprendi nesta aula

Nesta aula aprendi que strings possuem vários métodos e funções que permitem manipular textos de diferentes maneiras.

Alguns dos principais recursos:

| Recurso | Para que serve |
|---|---|
| `len()` | Conta os caracteres |
| `count()` | Conta ocorrências |
| `find()` | Procura uma parte do texto |
| `in` | Verifica se algo existe no texto |
| `replace()` | Substitui parte do texto |
| `upper()` | Coloca em maiúsculas |
| `lower()` | Coloca em minúsculas |
| `capitalize()` | Primeira letra maiúscula |
| `title()` | Primeira letra de cada palavra maiúscula |
| `strip()` | Remove espaços das extremidades |
| `split()` | Divide o texto |
| `join()` | Junta textos |
| `[]` | Permite acessar partes da string |

---

# 🏨 Aplicação no HotelHub

O conteúdo desta aula será muito útil para o HotelHub.

Por exemplo, quando um hóspede digitar o nome:

```python
nome = input('Nome do hóspede: ')
```

Podemos organizar o texto:

```python
nome = nome.strip()
nome = nome.title()
```

Assim, se a pessoa digitar:

```text
   joão da silva
```

podemos deixar:

```text
João Da Silva
```

Também podemos verificar informações digitadas pelo usuário.

Por exemplo:

```python
cidade = input('Cidade: ')

print('Rio' in cidade)
```

Isso pode ser útil futuramente para validar informações no sistema.

---

# 💡 O que achei importante nesta aula

Uma coisa que percebi é que o Python possui várias ferramentas para trabalhar com textos.

Antes eu poderia receber um texto do usuário e simplesmente mostrar na tela.

Agora consigo:

- Limpar espaços
- Alterar letras maiúsculas e minúsculas
- Procurar palavras
- Substituir informações
- Separar palavras
- Juntar textos
- Contar caracteres

Isso será muito importante para trabalhar com informações dos hóspedes no HotelHub.

---

# 🚀 Próximo passo

Continuar praticando a manipulação de strings e aplicar esses conhecimentos nos exercícios.

Também vou utilizar o conteúdo aprendido para melhorar o **HotelHub** conforme o projeto for evoluindo.

---
