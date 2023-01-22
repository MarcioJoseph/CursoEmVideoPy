maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("Peso da {}ª pessoa: ".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O \033[34mmaior\033[m peso lido foi de \033[34m{}Kg\033[m'.format(maior))
print('O \033[32mmenor\033[m peso lido foi de \033[32m{}Kg\033[m'.format(menor))
