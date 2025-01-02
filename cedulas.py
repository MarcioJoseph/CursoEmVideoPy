n = int(input())
notas_100 = notas_50 = notas_20 = notas_10 = notas_5 = notas_2 = notas_1 = 0
print(n)

while n > 0:
    if n >= 100:
        notas_100 += 1
        n -= 100
    elif n >= 50:
        notas_50 += 1
        n -= 50
    elif n >= 20:
        notas_20 += 1
        n -= 20
    elif n >= 10:
        notas_10 += 1
        n -= 10
    elif n >= 5:
        notas_5 += 1
        n -= 5
    elif n >= 2:
        notas_2 += 1
        n -= 2
    else:
        notas_1 += 1
        n -= 1

print(f"{notas_100} nota(s) de R$ 100,00")
print(f"{notas_50} nota(s) de R$ 50,00")
print(f"{notas_20} nota(s) de R$ 20,00")
print(f"{notas_10} nota(s) de R$ 10,00")
print(f"{notas_5} nota(s) de R$ 5,00")
print(f"{notas_2} nota(s) de R$ 2,00")
print(f"{notas_1} nota(s) de R$ 1,00")

n = int(input())
valor = n
notas = [100, 50, 20, 10, 5, 2, 1]
cont = 0
print(valor)
for i in range(len(notas)):
    cont = n // notas[i]
    n %= notas[i]
    print('{} nota(s) de R$ {},00'.format(cont,notas[i]))