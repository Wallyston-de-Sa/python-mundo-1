# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor. 
num = int(input('Digite um número: '))
sucessor = num + 1
antecessor = num - 1
print('O número escolhido é o {}.\nSeu sucessor é o {}.\nSeu antecessor é {}.'.format(num, sucessor, antecessor))