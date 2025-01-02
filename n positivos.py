valores = []
for i in range(6):
    valor = float(input(i+1))
    valores.append(valor)

valores_positivos = [v for v in valores if v > 0]

quantidade_positivos = len(valores_positivos)
print(f"{quantidade_positivos} valores positivos")


valoresPositivos = 0
for i in range(6):
    valor = float(input())
    if valor > 0:
        valoresPositivos += 1

print(f"{valoresPositivos} valores positivos")

