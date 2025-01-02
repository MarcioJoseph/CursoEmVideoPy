#maiorAB = (a+b+abs(a-b)) / 2

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

maiorab = (a+b+abs(a-b)) / 2
maior = (maiorab + c + abs(maiorab-c)) / 2
maior = int(maior)

print(f"{maior} eh o maior ")

