n = int(input())

# inicializa contadores para as cobaias
total_cobaias = 0
total_coelhos = 0
total_ratos = 0
total_sapos = 0

# lê os dados de cada caso de teste
for _ in range(n):
    entrada = input().split()
    quantia = int(entrada[0])
    tipo = entrada[1]

    total_cobaias += quantia

    if tipo == "c":
        total_coelhos += quantia
    elif tipo == "r":
        total_ratos += quantia
    elif tipo == "s":
        total_sapos += quantia

# calcula os percentuais

percentual_coelhos = (total_coelhos / total_cobaias) * 100
percentual_ratos = (total_ratos / total_cobaias) * 100
percentual_sapos = (total_sapos / total_cobaias) * 100

# mostra os resultados
print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percuntual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percuntual de ratos: {percentual_ratos:.2f} %")
print(f"Percuntual de sapos: {percentual_sapos:.2f} %")
