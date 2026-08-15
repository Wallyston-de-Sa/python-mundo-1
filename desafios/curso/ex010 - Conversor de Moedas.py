# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1.00 = R$3.27

# Entrada de dados
din = float(input('Qual valor você deseja trocar? R$'))

# Processamento
conversao = din / 3.27

# Saída de resultados
print('Com R${:.2f} você consegue cambear por US${:.2f}'.format(din, conversao))