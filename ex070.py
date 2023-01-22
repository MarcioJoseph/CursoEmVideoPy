#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
total = mais1000 = menor = cont = 0
barato = ''
print('-'*20)
print(f'Loja super baratão')
print('-'*20)
while True:
    prod = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    resp = ' '
    total += preço
    if preço > 1000:
        mais1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = prod
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' \033[34mFIM DO PROGRAMA\033[m '))
print(f'O total da compra foi \033[33mR${total:.2f}\033[m')
print(f'Temos {mais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi \033[31m{barato}\033[m que custa \033[31mR${menor:.2f}\033[m')
