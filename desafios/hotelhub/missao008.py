# Vamos melhorar a missão anterior de disponibilidade. Crie um programa que peça: Número do quarto, Nome do hóspede, Se o quarto está disponível (S/N). Depois, mostre o resumo usando cores no terminal:

cores = {
    'limpa' : '\033[m',
    'vermelho' : '\033[31m',
    'verde' : '\033[32m'
}
num = int(input('Quarto: '))
cliente = str(input('Hóspede: ')).strip().title()
vaga = str(input('O quarto está disponível S/N: ')).upper()

print('========== HOTELHUB ==========')
print('\nQuarto: {}'.format(num))
print('Hóspede: {}\n'.format(cliente))
if vaga == 'S':
    print('{}Quarto disponível!{}'.format(cores['verde'], cores['limpa']))
    print('{}Reserva liberada.{}'.format(cores['verde'],cores['limpa']))
else:
    print('{}Quarto indisponível!{}'.format(cores['vermelho'], cores['limpa']))
    print('{}Não é possível realizar a reserva.{}'.format(cores['vermelho'], cores['limpa']))
