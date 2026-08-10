# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan

angulo = float(input('Digite um ângulo qualquer: '))

# Converter para radianos
radiano = radians(angulo)

# Calcular seno, cosseno e tangente
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

#Saída
print('Seno de {}º é {:.4f}'.format(angulo, seno))
print('Cosseno de {}º é {:.4f}'.format(angulo, cosseno))
print('Tangente de {}º é {:.4f}'.format(angulo, tangente))