# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from calendar import isleap
ano = int(input('Digite um ano: '))
if isleap(ano):
    print('O ano é BISSEXTO')
else:
    print('O ano não é BISSEXTO')

