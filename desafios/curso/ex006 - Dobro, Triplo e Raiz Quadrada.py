# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# Entrada de dados
num = int(input('Digite um número: '))

# Processamento
do = num * 2
tri = num * 3
raiz = num ** (1/2)

# Saída de resultad
print('O número escolhido foi: {}.\nSeu dobro é {}.\nSeu triplo é {}.\nSua raiz quadrada é {:.2f}.'.format(num, do, tri, raiz))