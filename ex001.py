nome = input("Escreva o seu nome ? ")
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'roxo':'\033[35m',
         }
print("É um grande prazer em te conhecer {}{}{}, ".format(cores['verde'], nome, cores['limpa']))
