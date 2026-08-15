# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidoade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

# Entrada de dados
dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

# Processamento
valor = (dia * 60) + (km * 0.15)

# Saída de dados
print('O total a pagar é de R${:.2f}'.format(valor))
