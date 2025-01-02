salario = float(input())

if 0 < salario <= 400:
    reajuste = salario * 15 / 100
elif 400.01 <= salario <= 800:
    reajuste = salario * 12 / 100
elif 800.01 <= salario <= 1200:
    reajuste = salario * 10 / 100
elif 1200.01 <= salario <= 2000:
    reajuste = salario * 7 / 100
else:
    reajuste = salario * 4 / 100

novo_sal = salario + reajuste

print(f"Novo salario: {novo_sal:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"em percentual: {int(reajuste / salario * 100)}%")

salario = float(input())

tabela = [
    (0, 400.00, 15),
    (400.01, 800.00, 12),
    (800.01, 1200.00, 10),
    (1200.01, 2000, 7),
    (2000.01, float("inf"), 4)
]

for faixa in tabela:
    if faixa[0] <= salario <= faixa[1]:
        percentual = faixa[2]
        break

reajuste = salario * (percentual / 100)
new_sal = salario + reajuste

print(f"Novo salario: {new_sal:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")
