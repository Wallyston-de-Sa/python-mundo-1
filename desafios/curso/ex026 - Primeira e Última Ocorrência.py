# Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A". Em que posição ela aparece a primeira vez. Em que posição ela aparece a última vez.

# Entrada de dados
frase = str(input('Digite uma frase: ')).strip().upper()

# Saída de dados e processamento
print('A letra "A" apareceu {} na frase.'.format(frase.count('A')))
print('A primeira letra "A" da frase apareceu na posição {}.'.format(frase.find('A') + 1))
print('A última letra "A" da frase apareceu na posição {}.'.format(frase.rfind('A') + 1))