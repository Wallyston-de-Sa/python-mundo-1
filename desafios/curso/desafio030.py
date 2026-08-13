# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200km e R$0.45 para viagens mais longas.
km = float(input('Qual é a distância da sua viagem em Km? '))
if km <= 200:
    valor = km * 0.50
    print('Você vai viajar a {}Km de distância. O valor da viagem é de {:.2f}R$'.format(km, valor))
else:
    valor = km * 0.45
    print('Você vai viajar a {}Km de distância. O valor da viagem é de {:.2f}R$'.format(km, valor))