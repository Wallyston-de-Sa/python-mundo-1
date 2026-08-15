# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# Entrada de dados
salario_funcionario = float(input('Qual é o seu salário? R$'))

# Processamento
aumento = salario_funcionario * (15/100)
salario_final = salario_funcionario + aumento

# Saída de dados
print('Seu salário de R${:.2f} com um aumento de 15%. Passa a ser de R${:.2f}'.format(salario_funcionario, salario_final))