# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

# Entrada de dados
nome = str(input('Qual é o seu nome? ')).strip().upper()

# Saída de resultados e processamento
print('Seu nome tem Silva? {}'.format('SILVA' in nome))