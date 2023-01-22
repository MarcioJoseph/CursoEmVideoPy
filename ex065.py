#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor
# valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
quant = soma = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    quant += 1
    soma += num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
media = soma / quant
print('Você digitou \033[32m{}\033[m números e a média foi \033[32m{:.2f}\033[m'.format(quant, media))
print('O maior número foi \033[31m{}\033[m e o menor número foi \033[31m{}\033[m'.format(maior, menor))
