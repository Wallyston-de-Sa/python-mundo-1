# Usado pelo professor para economizar memorias.
preco = float(input('Qual é o valor do produto? R$'))
desconto = preco - (preco * 5 / 100)
print('O produto inserido custa R${:.2f}. O preço final sairá por {:.2f}!'.format(preco, desconto))