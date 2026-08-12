# Crie um programa que receba o nome completo de um hóspede e mostre algumas informações sobre ele. O HotelHub deve mostrar: Nome completo em MAIÚSCULAS. Nome completo em minúsculas. Quantidade de caracteres do nome sem contar os espaços. Primeiro nome. Último nome.
print('========== HOTELHUB ==========')
#Variavel
nome = str(input('Nome do hóspede: ')).strip()
print('\n============ INFORMAÇÕES ============\n')
# Manipulação de string
lista = nome.split()
#Saida de Resultados
print('Nome em maiúsculo: {}'.format(nome.upper()))
print('Nome em minúsculo: {}'.format(nome.lower()))
print('Caracteres sem espaços: {}'.format(len(nome.replace(' ', ''))))
print('Primeiro nome: {}'.format(lista[0]))
print('Último nome: {}'.format(lista[-1]))