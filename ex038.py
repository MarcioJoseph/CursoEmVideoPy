cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'roxo':'\033[35m',
         }

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('o PRIMEIRO é maior'.format(cores['verde']))
elif n1 < n2:
    print('O SEGUNDO é maior')
else:
    print('Os valores são IGUAIS')
