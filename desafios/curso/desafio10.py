# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1.00 = R$3.27
din = float(input('Qual valor você deseja trocar? R$'))
conversao = din / 3.27
print('Com R${:.2f} você consegue cambear por US${:.2f}'.format(din, conversao))