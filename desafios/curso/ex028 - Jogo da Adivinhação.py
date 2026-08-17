# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

# Entrada de dados
print('=-=' * 20)
print('Vou penar em um número entre 0 e 5. Tente adivinhar...')
print('=-=' * 20)
jogador = int(input('Em que número eu pensei? '))

# Processamento
print('Aguarde um pouco...')
pensar = randint(0, 5)
sleep(2)

# Saída de resultados e processamento
print('Pensei no número {} e você chutou no {}.'.format(pensar, jogador))
if jogador == pensar:
    print('Você acertou! Ganhou o jogo. Parabéns!!')
else:
    print('Você errou! Tente novamente. Não desista!')