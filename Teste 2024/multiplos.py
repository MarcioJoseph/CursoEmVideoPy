a, b = map(int, input().split())

if a % b == 0 or b % a == 0:
    print("é multiplo ")
else:
    print("não é multiplos")