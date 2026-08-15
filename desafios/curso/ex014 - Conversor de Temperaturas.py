# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

# Entrada de dados
c = float(input('Informe a temperatura em ºC: '))

# Processamento
f = 9 * c / 5 + 32

# Saída de dados
print('A temperatura de {}ºC corresponde a {}ºF!'.format(c, f))