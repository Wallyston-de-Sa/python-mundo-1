# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# Entrada de dados
num = int(input('Digite um número: '))

# Processamento e saída de resultados
if num % 2 == 0:
    print('O número {} é PAR.'.format(num))
else:
    print('O número {} É IMPAR.'.format(num))