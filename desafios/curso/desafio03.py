#Crie um script Python que leia dois números e tente mostrar a soma entre eles.
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
print('A soma é', (num1+num2))

# Outra forma ensinada
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
soma = num1 + num2
print('A soma entre o número {} e o número {} vale {}'.format(num1, num2, soma))