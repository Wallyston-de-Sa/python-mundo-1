#Cadastro de Usuario

# Cores
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'magenta': '\033[35m',
    'ciano': '\033[36m'
}

# Entrada de dados
nome = input('{}Qual é o seu nome?{} '.format(cores['ciano'], cores['limpa']))
idade = int(input('{}Qual é a sua idade?{} '.format(cores['ciano'], cores['limpa'])))
cidade = input('{}Qual cidade você mora?{} '.format(cores['ciano'], cores['limpa']))

# Saída de resultados
print('{}===== HOTELHUB ====={}\n'.format(cores['magenta'], cores['limpa']))
print('{}Hóspede cadastrado com sucesso!{}\n'.format(cores['verde'], cores['limpa']))
print('{}Nome: {}{}'.format(cores['azul'], nome, cores['limpa']))
print('{}Idade: {}{}'.format(cores['azul'], idade, cores['limpa']))
print('{}Cidade: {}{}'.format(cores['azul'], cidade, cores['limpa']))
