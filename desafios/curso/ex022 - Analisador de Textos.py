# Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas. O nome com todas minúsculas. Quantas letras ao todo (sem considerar espaços). Quantas letras tem o primeiro nome

# Entrada de dados
nome = str(input('Digite seu nome: ')).strip()

# Processamento
# Manipulando entre maiúsculo e minúsculo
maiusculo = nome.upper()
minusculo = nome.lower()
# Manipulando os espaços no nome
espaco = len(nome.replace(' ', ''))
# Manipulando o texto e criando uma lista para leitura do primeiro nome
lista = len(nome.split()[0])

# Saída de resultados
print('Seu primeiro nome tem: {} caracteres.'.format(lista))
print('Seu nome todo em MAIÚSCULO: {}\nSeu nome todo em minúsculo: {}'.format(maiusculo, minusculo))
print('Seu nome sem os espaços contém: {} caracteres.'.format(espaco))