# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Velocidade do veiculo em Km/h: '))
limite = 80
if velocidade > limite:
    excesso = velocidade - limite
    multa = excesso * 7.00
    print('Você está em alta velocidade para a via! Você foi multado em {:.2f}R$'.format(multa))
else:
    print('Você está com a velocidade permitida para a via!')
