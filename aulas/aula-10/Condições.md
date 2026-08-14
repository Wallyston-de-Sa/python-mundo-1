# Curso de Python - Mundo 1
## Aula 10 - Condições

Nesta aula comecei a aprender como fazer o Python **tomar decisões**.

Até agora, meus programas basicamente recebiam informações e mostravam resultados.

Com as condições, consigo fazer o programa analisar uma situação e escolher o que fazer.

---

# `if`

O `if` significa **"se"**.

Ele executa um bloco de código somente quando uma condição é verdadeira.

Exemplo:

```python
idade = 18

if idade >= 18:
    print('Você é maior de idade.')
```

Nesse caso, como `18 >= 18` é verdadeiro, a mensagem será exibida.

---

# `else`

O `else` significa **"senão"**.

Ele é utilizado quando queremos executar outro código caso a condição do `if` seja falsa.

```python
idade = 16

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')
```

Como a idade é menor que 18, o programa executa o `else`.

---

# `elif`

O `elif` significa **"senão, se"**.

Ele permite verificar uma nova condição caso a anterior seja falsa.

```python
idade = 18

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Acabou de completar 18 anos')
else:
    print('Maior de idade')
```

Podemos utilizar vários `elif` quando necessário.

---

# Operadores de comparação

As condições utilizam operadores para comparar valores.

| Operador | Significado |
|---|---|
| `==` | Igual |
| `!=` | Diferente |
| `>` | Maior que |
| `<` | Menor que |
| `>=` | Maior ou igual |
| `<=` | Menor ou igual |

### Exemplos

```python
5 == 5
```

Resultado:

```text
True
```

```python
5 != 3
```

Resultado:

```text
True
```

```python
10 > 5
```

Resultado:

```text
True
```

```python
3 < 2
```

Resultado:

```text
False
```

---

# `and`

O operador `and` significa **"e"**.

As duas condições precisam ser verdadeiras.

```python
idade = 25
documento = True

if idade >= 18 and documento:
    print('Entrada permitida.')
```

Nesse caso, as duas condições precisam ser verdadeiras para o `if` ser executado.

---

# `or`

O operador `or` significa **"ou"**.

Nesse caso, basta uma das condições ser verdadeira.

```python
dia = 'sábado'

if dia == 'sábado' or dia == 'domingo':
    print('É final de semana.')
```

---

# `not`

O operador `not` inverte o resultado de uma condição.

Por exemplo:

```python
disponivel = False

if not disponivel:
    print('Quarto indisponível.')
```

---

# Condições com `input()`

Podemos utilizar informações digitadas pelo usuário para tomar decisões.

```python
idade = int(input('Qual sua idade? '))

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')
```

Isso deixa o programa mais interativo.

---

# Exemplo com números

Podemos verificar se um número é par ou ímpar.

```python
num = int(input('Digite um número: '))

if num % 2 == 0:
    print('O número é par.')
else:
    print('O número é ímpar.')
```

O operador `%` mostra o resto da divisão.

Se o resto da divisão por 2 for `0`, o número é par.

---

# Exemplo com três valores

Na aula também aprendi a utilizar condições para comparar valores.

```python
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('O maior valor é {}'.format(a))
elif b > a and b > c:
    print('O maior valor é {}'.format(b))
else:
    print('O maior valor é {}'.format(c))
```

---

# Exemplo: formando um triângulo

Um dos exercícios que fiz foi verificar se três medidas podem formar um triângulo.

```python
med1 = float(input('Digite a primeira medida: '))
med2 = float(input('Digite a segunda medida: '))
med3 = float(input('Digite a terceira medida: '))

if med1 < med2 + med3 and med2 < med1 + med3 and med3 < med1 + med2:
    print('É um triangulo.')
else:
    print('Não é um triangulo.')
```

A condição verifica se cada lado é menor que a soma dos outros dois.

---

# Indentação

Uma coisa muito importante que aprendi nesta aula é a **indentação**.

Depois de um `if`, `elif` ou `else`, o código que pertence à condição precisa estar indentado.

Correto:

```python
if idade >= 18:
    print('Maior de idade')
```

O espaço antes do `print()` mostra que ele pertence ao `if`.

---

# 🏨 Aplicando no HotelHub

Nesta aula consegui evoluir o HotelHub.

Antes, o programa apenas recebia informações e mostrava os resultados.

Agora ele consegue **tomar decisões**.

Na Missão 007, criei uma verificação para saber se um quarto está disponível:

```python
num = int(input('Quarto: '))
nome = str(input('Nome do hóspede: ')).strip().title()
disponivel = str(input('S/N: ')).upper()

print('========== HOTELHUB ===========\n')
print('Quarto: {}'.format(num))
print('Hóspede: {}\n'.format(nome))

if disponivel == 'S':
    print('Quarto disponível!\nReserva liberada.')
else:
    print('Quarto indisponível!\nNão é possível realizar a reserva.')

print('=' * 31)
```

Agora o HotelHub consegue analisar a resposta do usuário e apresentar uma mensagem diferente dependendo da situação.

---

# 💡 O que achei mais importante nesta aula

Acredito que essa foi uma das aulas mais importantes até agora.

Com `if`, `elif` e `else`, os programas deixam de apenas executar comandos em sequência e começam a **tomar decisões**.

Isso será muito importante para continuar desenvolvendo o HotelHub.

No futuro, poderei usar condições para verificar coisas como:

- Se um quarto está disponível
- Se um hóspede pode fazer determinado cadastro
- Se uma reserva está válida
- Se um pagamento foi realizado
- Se existe algum quarto disponível
- Se determinada informação está correta

---

# O que aprendi

Nesta aula aprendi:

- `if`
- `elif`
- `else`
- Operadores de comparação
- `and`
- `or`
- `not`
- Condições com `input()`
- Comparação de números
- Tomada de decisões
- Importância da indentação

---

# 🏨 HotelHub

Missão realizada:

- [x] Missão 007 - Disponibilidade do quarto

---

# Conclusão

A Aula 10 foi um passo importante na minha aprendizagem.

Agora consigo criar programas que não apenas recebem e exibem informações, mas também **analisam situações e tomam decisões**.

O próximo objetivo é continuar praticando as condições e utilizar esse conhecimento para deixar o HotelHub cada vez mais próximo de um sistema real.

---
