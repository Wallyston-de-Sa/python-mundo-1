# Disponibilidade do quarto
num = int(input('Quarto: '))
nome = str(input('Nome do hóspede: ')).strip().title()
disponivel = str(input('S/N: ')).upper().strip()

print('========== HOTELHUB ===========\n')
print('Quarto: {}'.format(num))
print('Hóspede: {}\n'.format(nome))
if disponivel == 'S':
    print('Quarto disponível!\nReserva liberada.')
else:
    print('Quarto indisponível!\nNão é possível realizar a reserva.\n')
print('='*31)
