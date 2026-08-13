# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a 
# R$1.250.00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o salário que você ganha: R$'))

if salario > 1250:
    aumento = salario + (salario * (10/100))
    print('Com aumento de 10%. Seu salário será de R${:.2f}'.format(aumento))
else:
    aumento = salario + (salario * (15/100))
    print('Com aumento de 15%. Seu salário será de R${:.2f}'.format(aumento))