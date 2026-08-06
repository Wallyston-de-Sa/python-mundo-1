hospede = input('Nome do hóspede: ')
diaria = float(input('Valor da diária: R$'))
qntdia = int(input('Quantidade de diárias: '))
total = diaria * qntdia

print('========== HOTELHUB ==========')
print('Hóspede: {}'.format(hospede))
print('\nValor da diária: R${:.2f}\nQuantidade de diárias: {}\n\nValor total da hospedagem: R${:.2f}'.format(diaria, qntdia, total))
