# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# Entrada de dados
preco = float(input('Qual é o valor do produto? R$'))

# processamento
desconto = preco * (5 / 100)
preco_final = preco - desconto

# Saída de resultados
print('O produto inserido custa R${:.2f}. O valor do desconto será de {:.2f}. O preço final sairá por {:.2f}!'.format(preco, desconto, preco_final))