# Calculo da área do quarto
from math import hypot
quarto = int(input('Quarto: '))
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
area = largura * comprimento
diagonal = hypot(largura, comprimento)

print('========= HOTELHUB =========')
print('Quarto: Suite {}'.format(quarto))
print('Largura: {} m'.format(largura))
print('Comprimento: {} m'.format(comprimento))
print('\nÁrea do quarto: {} m²'.format(area))
print('Diagonal do quarto: {:.2f} m'.format(diagonal))
print('='*28)