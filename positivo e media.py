valores = [float(input()) for _ in range(6)]

positivos = [v for v in valores if v > 0]

quantidade_positivos = len(positivos)

media_positivos = sum(positivos) / quantidade_positivos if quantidade_positivos > 0 else 0

print(quantidade_positivos)
print(f"{media_positivos:.1f}")

