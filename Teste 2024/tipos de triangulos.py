a, b, c = map(float, input().split())

valores_ordenados = sorted([a, b, c], reverse=True)
a, b, c = valores_ordenados

if a >= b + c:
    print("NÃO FORMA TRIANGULO")
elif a ** 2 == b ** 2 + c ** 2:
    print("TRIANGULO RETANGULO")
elif a ** 2 > b ** 2 + c ** 2:
    print("TRIANGULO OBTUSANGULO")
elif a ** 2 < b ** 2 + c ** 2:
    print("TRIANGULO ACUTANGULO")
if a == b == c:
    print("TRIANGULO EQUILATERO")
elif a == b or b == c or a == c:
    print("triangulo isosceles")


