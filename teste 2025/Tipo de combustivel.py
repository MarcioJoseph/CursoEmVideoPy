n = 0
alcool=gasolina=diesel = 0

while n != 4:
    n = int(input())
    while 1 > n > 4:
        n = int(input())
    if n == 1:
        alcool += 1
    elif n == 2:
        gasolina += 1
    elif n == 3:
        diesel += 1
print(f'MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')
