#Cadastro de quarto
num = int(input('Número do quarto: '))
quarto = str(input('Tipo do quarto: '))
valor = float(input('Valor da diária:R$ '))
vago = str(input('Está disponível? (S/N)'))

print('======= HOTELHUB =======')

print('Quarto cadastrado!')

print('Número: {}\nTipo: {}\nDiária: R${}\nDisponível: {}'.format(num, quarto, valor, vago))