valor_a = int(input())
valor_b = int(input())

if valor_a > valor_b:
    valor_a, valor_b = valor_b, valor_a

soma_impares = sum(i for i in range(valor_a +1, valor_b) if i % 2 != 0)

print(soma_impares)
