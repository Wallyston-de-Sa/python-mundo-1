# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

# Entrada de dados
cidade = str(input('Em qual cidade você nasceu? ')).strip().upper()

# Processamento
inicio = (cidade.split())

# Saída de dados
print('SANTO' in inicio[0])
