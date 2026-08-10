# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
oposto = float(input('Qual é o comprimento do cateto oposto? '))
adjacente = float(input('Qual é o comprimento do cateto adjacente? '))
hipotenusa = hypot(oposto, adjacente)
print('A hipotenusa é {}'.format(hipotenusa))