valores = [int(input()) for _ in range(5)]

pares = [v for v in valores if v % 2 == 0]
pares = len(pares)

print(f"{pares} valores pares")
