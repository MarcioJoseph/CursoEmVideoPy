while True:
    try:
        m, n = map(int, input().split())
    except EOFError:
        break
    if m <= 0 or n <= 0:
        break

    if m < n:
        menor = m
        maior = n
    else:
        menor = n
        maior = m

    sequencia = []
    soma = 0
    for i in range(menor, maior +1):
        sequencia.append(i)
        soma += i

    print(*sequencia, f'Sum={soma}')
