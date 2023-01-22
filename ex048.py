# Faça um programa que calcule a soma entre todos os números que são múltiplos de 3 e que se encontra
#no intervalo de 1 até 500.
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1 # cont + 1
        soma += c # soma + c
print('A SOMA de todos os {} valores solicitados é {}'.format(cont, soma))
