# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan

# Entrada de dados
angulo = float(input('Digite um ângulo qualquer: '))

# Processamento
radiano = radians(angulo) # Precisa converter para radiano e depois formar em seno, cosseno e tangente
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

# Saída de resultados
print('Seno de {}º é {:.2f}'.format(angulo, seno))
print('Cosseno de {}º é {:.2f}'.format(angulo, cosseno))
print('Tangente de {}º é {:.2f}'.format(angulo, tangente))