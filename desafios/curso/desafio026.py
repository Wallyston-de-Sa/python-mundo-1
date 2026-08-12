# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. EX: Ana Maria de Souza. Primeiro: Ana. Último: Souza.
nome = str(input('Digite seu nome completo: ')).strip()

# Manipulação de string
lista = nome.split()

# Manipulação e resultado
print('Seu primeiro nome é {}'.format(lista[0]))
print('Seu último nome é {}'.format(lista[len(lista)-1]))
