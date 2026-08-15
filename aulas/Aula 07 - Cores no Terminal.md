# Curso de Python - Mundo 1
## Aula 11 - Cores no Terminal

Nesta aula aprendi como utilizar **cores no terminal** utilizando códigos especiais do Python.

As cores podem deixar os programas mais organizados e facilitar a visualização das informações.

---

# Códigos ANSI

Para colocar cores no terminal, podemos utilizar códigos ANSI.

Um exemplo:

```python
print('\033[31mOlá, mundo!\033[m')
```

Nesse exemplo:

- `\033[` inicia o código de cor
- `31m` define a cor vermelha
- `\033[m` limpa a formatação e volta ao padrão

---

# Algumas cores

Existem vários códigos de cores que podemos utilizar.

| Código | Cor |
|---|---|
| `30` | Preto |
| `31` | Vermelho |
| `32` | Verde |
| `33` | Amarelo |
| `34` | Azul |
| `35` | Roxo |
| `36` | Ciano |
| `37` | Branco |

Exemplo:

```python
print('\033[31mVermelho\033[m')
print('\033[32mVerde\033[m')
print('\033[33mAmarelo\033[m')
print('\033[34mAzul\033[m')
```

---

# Estilos do texto

Além das cores, também podemos alterar o estilo do texto.

Alguns códigos:

| Código | Estilo |
|---|---|
| `0` | Sem estilo |
| `1` | Negrito |
| `4` | Sublinhado |
| `7` | Inverte as cores |

Exemplo:

```python
print('\033[1mTexto em negrito\033[m')
```

---

# Utilizando mais de uma configuração

Podemos combinar estilo e cor.

Por exemplo:

```python
print('\033[1;31mTexto vermelho em negrito\033[m')
```

Nesse caso:

- `1` → negrito
- `31` → vermelho

---

# Fundo colorido

Também podemos alterar a cor do fundo.

Alguns códigos:

| Código | Cor do fundo |
|---|---|
| `40` | Preto |
| `41` | Vermelho |
| `42` | Verde |
| `43` | Amarelo |
| `44` | Azul |
| `45` | Roxo |
| `46` | Ciano |
| `47` | Branco |

Exemplo:

```python
print('\033[30;42mTexto preto com fundo verde\033[m')
```

---

# Estrutura do código

Uma forma de entender o código é:

```text
\033[estilo;cor;fundo m
```

Por exemplo:

```python
print('\033[1;34;40mOlá, mundo!\033[m')
```

Nesse caso:

- `1` → negrito
- `34` → azul
- `40` → fundo preto
- `\033[m` → volta ao padrão

---

# Criando variáveis para as cores

Se utilizarmos muitas cores no programa, podemos criar variáveis para facilitar.

```python
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m'
}
```

Depois podemos utilizar:

```python
print('{}Texto verde{}'.format(cores['verde'], cores['limpa']))
```

Isso pode deixar o código mais fácil de organizar quando o programa começa a crescer.

---

# ⚠️ Por que usar `\033[m`?

É importante lembrar de finalizar a formatação.

Por exemplo:

```python
print('\033[31mTexto vermelho\033[m')
print('Texto normal')
```

O `\033[m` faz o terminal voltar para a configuração normal.

Isso evita que todos os textos seguintes continuem com a mesma cor.

---

# 🏨 Aplicando no HotelHub

O conteúdo desta aula pode ser muito útil para deixar o HotelHub mais organizado visualmente.

Por exemplo:

- 🟢 Verde → quarto disponível
- 🔴 Vermelho → quarto ocupado
- 🟡 Amarelo → aviso
- 🔵 Azul → informações
- ⚪ Normal → textos comuns

Por exemplo:

```python
print('\033[32mQuarto disponível!\033[m')
```

ou:

```python
print('\033[31mQuarto indisponível!\033[m')
```

Assim, o usuário consegue identificar as informações importantes mais rapidamente.

---

# 💡 O que aprendi nesta aula

Nesta aula aprendi que podemos utilizar códigos ANSI para modificar a aparência dos textos no terminal.

Aprendi a trabalhar com:

- Cores do texto
- Cores do fundo
- Negrito
- Sublinhado
- Combinação de estilos
- Reset da formatação
- Variáveis para organizar as cores

---

# 🧠 Uma coisa importante

Não preciso colocar cores em todos os textos do programa.

As cores devem ajudar na organização e na identificação das informações.

Por exemplo, no HotelHub faz sentido utilizar:

```text
Verde → disponível
Vermelho → ocupado
Amarelo → atenção
Azul → informação
```

Dessa forma, as cores possuem uma função dentro do sistema e não são apenas decoração.

---

# 🏨 HotelHub

A Aula 11 abre novas possibilidades para o HotelHub.

Agora posso começar a deixar o sistema mais agradável visualmente.

No futuro, posso utilizar cores para:

- Mostrar quartos disponíveis
- Mostrar quartos ocupados
- Destacar erros
- Mostrar avisos
- Destacar confirmações
- Organizar menus

---

# Conclusão

A Aula 11 me ensinou como utilizar cores e estilos no terminal.

Aprendi que os códigos ANSI permitem modificar a aparência dos textos e que posso combinar diferentes estilos e cores.

Também percebi que as cores podem ser úteis para melhorar a experiência de quem utiliza o programa.

O próximo passo é continuar praticando e utilizar esse conhecimento no **HotelHub**, sem exagerar nas cores.

---