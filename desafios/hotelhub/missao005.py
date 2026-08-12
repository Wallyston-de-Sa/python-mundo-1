#Crie um programa que permita cadastrar um hóspede no HotelHub. O programa deve pedir: Nome completo do hóspede, Idade, Número do quarto, Quantidade de dias da hospedagem. Depois, mostre um resumo do cadastro.

# Váriaveis
print('========= HOTELHUB =========')
nome = str(input('Nome do hóspede: ')).strip().title()
idade = int(input('Idade: '))
quarto = int(input('Quarto: '))
dias = int(input('Dias: '))

# Saída de Resultados
print('========= RESUMO =========')
print('\nHóspede: {}'.format(nome))
print('Idade: {} anos'.format(idade))
print('Quarto: {}'.format(quarto))
print('Hospedagem: {} dias'.format(dias))
print('\n==========================')

