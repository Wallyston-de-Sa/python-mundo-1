# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
pensar = randint(0, 5)
print('========= JOGO DA SORTE =============')
computador = int(input('Estou pensando em um número. Tente acertar é entre 0 e 5: '))
if computador == pensar:
    print('Você acertou! Ganhou o jogo. Parabéns!!')
else:
    print('Você errou! Tente novamente. Não desista!')