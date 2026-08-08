# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
me = float(input('Digite um valor em metros: '))
ce = me * 100
mi = me * 1000
print('{} metros.\n{:.2f} centímetros.\n{:.2f} milímetros.'.format(me, ce, mi))