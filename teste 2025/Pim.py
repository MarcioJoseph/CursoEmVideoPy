n = int(input())
cont = 0
a,b,c = 1,2,3
while cont < n:
    print(f'{a} {b} {c} PIM')
    c += 2
    a = c
    b = c
    b += 1
    c += 2
    cont += 1
