# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2) / 2
print('Sua primeira nota foi {:.1f} e sua segunda foi {:.1f}. Sua média final é {:.1f}.'.format(n1, n2, media))