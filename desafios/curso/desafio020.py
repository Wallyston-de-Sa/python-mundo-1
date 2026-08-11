# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
a1 = str(input('Nome do aluno: '))
a2 = str(input('Nome do aluno: '))
a3 = str(input('Nome do aluno: '))
a4 = str(input('Nome do aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A apresentação será: {}'.format(lista))