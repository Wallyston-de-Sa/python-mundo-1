# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# Entrada de dados
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

# Processamento
media = (n1+n2) / 2

# Saída de resultados
print('Sua primeira nota foi {:.1f} e sua segunda foi {:.1f}. Sua média final é {:.1f}.'.format(n1, n2, media))