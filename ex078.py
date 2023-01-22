# Exercício Python 078: Faça um programa que leia 5 valores numéricos e
# guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e
# as suas respectivas posições na lista.
menor = 0
maior = 0
listanúm = []
for c in range(0, 5):
    listanúm.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        menor = maior = listanúm[c]
    else:
        if listanúm[c] > maior:
            maior = listanúm[c]
        if listanúm[c] < menor:
            menor = listanúm[c]
print('=-' * 30)
print(f'Voce digitou os valores {listanúm}')
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanúm):
    if v == menor:
        print(f'{i}...', end='')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanúm):
    if v == maior:
        print(f'{i}...', end='')
print()
