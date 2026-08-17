# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot

# Entrada de dados
oposto = float(input('Qual é o comprimento do cateto oposto? '))
adjacente = float(input('Qual é o comprimento do cateto adjacente? '))

# Processamento
hipotenusa = hypot(oposto, adjacente)

# Saída de resultados
print('A hipotenusa é {:.2f}'.format(hipotenusa))