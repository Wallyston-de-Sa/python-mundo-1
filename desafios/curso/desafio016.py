# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: 'O número 6.127 tem a parte inteira 6.
from math import floor
num = float(input('Digite um número real: '))
print('O número {} tem a parte inteira {}'.format(num, floor(num)))