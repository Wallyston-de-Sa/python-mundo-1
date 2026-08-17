# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. EX: Ana Maria de Souza. Primeiro: Ana. Último: Souza.

# Entrada de dados
nome = str(input('Digite seu nome completo: ')).strip()

# Processamento
lista = nome.split()

# Saída de dados e processamento
print('Seu primeiro nome é {}'.format(lista[0]))
print('Seu último nome é {}'.format(lista[len(lista)-1]))
