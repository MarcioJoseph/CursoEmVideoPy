'''valor = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
cont = 0
print("NOTAS: ")
for i in range(len(notas)):
    cont = valor // notas[i]
    valor %= notas[i]
    cont = int(cont)
    print(f'{cont} nota(s) de R$ {notas[i]}.00')
print('MOEDAS: ')
for i in range(len(moedas)):
    cont = valor // moedas[i]
    valor %= moedas[i]
    cont = int(cont)
    print(f"{cont} moeda(s) de R$ {moedas[i]:.2f}")


N = float(input())

# Inicialização das notas e moedas disponíveis
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

# Inicialização das variáveis para contar notas e moedas
quantidade_notas = []
quantidade_moedas = []

# Cálculo das notas
for nota in notas:
    qtd = int(N // nota)
    quantidade_notas.append(qtd)
    N -= qtd * nota

# Cálculo das moedas
for moeda in moedas:
    qtd = int(N // moeda)
    quantidade_moedas.append(qtd)
    N -= qtd * moeda

# Impressão do resultado
print("NOTAS:")
for i, nota in enumerate(notas):
    print(f"{quantidade_notas[i]} nota(s) de R$ {nota:.2f}")

print("MOEDAS:")
for i, moeda in enumerate(moedas):
    print(f"{quantidade_moedas[i]} moeda(s) de R$ {moeda:.2f}")
'''

# Leitura do valor de ponto flutuante N
N = float(input())

# Inicialização das notas e moedas disponíveis
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

# Inicialização das variáveis para contar notas e moedas
quantidade_notas = []
quantidade_moedas = []

# Cálculo das notas
for nota in notas:
    qtd = int(N // nota)
    quantidade_notas.append(qtd)
    N -= qtd * nota

# Cálculo das moedas
for moeda in moedas:
    qtd = int(N // moeda)
    quantidade_moedas.append(qtd)
    N -= qtd * moeda

# Impressão do resultado
print("NOTAS:")
for i, nota in enumerate(notas):
    print(f"{quantidade_notas[i]} nota(s) de R$ {nota:.2f}")

print("MOEDAS:")
for i, moeda in enumerate(moedas):
    print(f"{quantidade_moedas[i]} moeda(s) de R$ {moeda:.2f}")