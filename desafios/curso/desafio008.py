# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
me = float(input('Digite um valor em metros: '))
dm = me * 10
ce = me * 100
mi = me * 1000
dam = me / 10
hm = me / 100
km = me / 1000
print('{}m corresponde a {:.0f} dm, {:.0f} cm, {:.0f} mm e {:.0f} dam, {:.0f} hm, {:.0f} km.'.format(me, dm, ce, mi, dam, hm, km))