# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
a1 = str(input('Qual nome do aluno? '))
a2 = str(input('Qual nome do aluno? '))
a3 = str(input('Qual nome do aluno? '))
a4 = str(input('Qual nome do aluno? '))
nomes = a1, a2, a3, a4
sorteio = choice(nomes)
print('O aluno sorteado foi: {}'.format(sorteio))