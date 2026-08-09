# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
num = int(input('Digite um número: '))
do = num * 2
tri = num * 3
raiz = num ** (1/2)
print('O número escolhido foi: {}.\nSeu dobro é {}.\nSeu triplo é {}.\nSua raiz quadrada é {:.2f}.'.format(num, do, tri, raiz))