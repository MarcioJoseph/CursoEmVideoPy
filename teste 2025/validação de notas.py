nota_valida = 0
x = 0
media = 0
while nota_valida != 2:
    x = float(input())
    if 0 <= x <= 10:
        media += x / 2
        nota_valida += 1
    else:
        print('nota invalida')

print(f"media = {media:.2f}")
