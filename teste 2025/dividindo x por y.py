n = int(input())

i = 0

while i < n:
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    if y == 0:
        print('divisão impossível')
    else:
        print(f'{x/y:.1f}')
    i += 1