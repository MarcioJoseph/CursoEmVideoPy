a, b, c = map(float, input().split())

if a < b + c and b < a + c and c < a + b:
    print(f"Perimetro = {a + b + c}")
else:
    print(f"Área = {(a + b) * c / 2}")
