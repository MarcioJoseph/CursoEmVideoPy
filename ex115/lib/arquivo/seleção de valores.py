'''a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if b > c and d > a and (c + d) > (a + b) and (c, d >= 0) and (a % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
'''
import math

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

delta = (b ** 2) - 4 * a * c

# ax² + bx + c=0   x = -b +- raiz(b² - 4*a*c)
                            #2*a

if a == 0:
    print("Impossivel calcular")
elif delta < 0:
    print("Impossivel calcular")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    #print("x1: {}, x2: {}".format(x1, x2))
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")