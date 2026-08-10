# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))
area = largura * altura
tinta = area / 2

print('A largura da parede é de {} metros.\nA altura é de {} metros.\nTotal em área é de {}m².\nSerá necessário {} litros de tinta.'.format(largura, altura, area, tinta))