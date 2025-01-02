num = int(input())

medias_ponderadas = []

for _ in range(num):
    valores = input().split()
    a = float(valores[0])
    b = float(valores[1])
    c = float(valores[2])

    media_ponderada = (a *2 + b * 3 + c * 5) / 10
    medias_ponderadas.append(media_ponderada)

for media in medias_ponderadas:
    print(f"{media:.1f}")

