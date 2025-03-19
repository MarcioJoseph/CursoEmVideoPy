i = 0
inter = 0
gremio = 0
empate = 0
cont = 0
inter_gols = 0
gremio_gols = 0

while i != 2:
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    if x > y:
        inter += 1
    elif y > x:
        gremio += 1
    elif y == x:
        empate += 1
    inter_gols += x
    gremio_gols += y
    print('novo grenal (1-sim 2-nao)')
    i = int(input())
    cont += 1

print(f'{cont} grenais')
print(f'Inter: {inter}')
print(f'Gremio: {gremio}')
print(f'Empates: {empate}')
print(f'Saldo de gols Inter: {inter_gols}')
print(f'Saldo de gols Gremio: {gremio_gols}')
if inter > gremio:
    print('Inter venceu mais.')
elif gremio > inter:
    print('Gremio venceu mais')
else:
    print('Confronto empatado')
