n = int(input())
for _ in range(n):
    X, Y = map(int, input().split())
    # Aqui você vai adicionar o código para processar X e Y
    if X > Y:
        X, Y = Y, X

    soma = 0
    for numero in range(X + 1, Y):
        if numero % 2 != 0:
            soma += numero

    print(soma)

