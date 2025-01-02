salario = float(input())

if 0 <= salario <= 2000.00:
    print("isento")
elif 2000.01 <= salario <= 3000.00:
    imposto = (salario - 2000) * 0.08
    print(f"R$ {imposto:.2f}")
elif 3000.01 <= salario <= 4500.00:
    imposto = (salario - 3000) * 0.18 + 80
    print(f"R$ {imposto:.2f}")
else:
    imposto = (salario - 4500) * 0.28 + 350
    print(f"R$ {imposto:.2f}")

