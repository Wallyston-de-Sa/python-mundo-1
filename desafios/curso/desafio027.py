# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
# variavel
pensar = randint(0, 5)

# interface
print('=-=' * 20)
print('Vou penar em um número entre 0 e 5. Tente adivinhar...')
print('=-=' * 20)

# variavel
jogador = int(input('Em que número eu pensei? '))

# interface e resultado
sleep(2)
print('Pensei no número {} e você chutou no {}.'.format(pensar, jogador))
if jogador == pensar:
    print('Você acertou! Ganhou o jogo. Parabéns!!')
else:
    print('Você errou! Tente novamente. Não desista!')