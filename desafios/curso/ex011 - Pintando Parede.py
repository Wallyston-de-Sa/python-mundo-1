# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².

# Entrada de dados
largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))

# Processamento
area = largura * altura
tinta = area / 2

# Saída de resultados
print('A largura da parede é de {} metros.'.format(largura))
print('A altura é de {} metros.'.format(altura))
print('Total em área é de {}m².'.format(area))
print('Será necessário {} litros de tinta.'.format(tinta))