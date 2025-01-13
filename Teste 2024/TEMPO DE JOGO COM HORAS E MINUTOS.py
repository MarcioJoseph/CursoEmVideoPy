entrada = input().split()
hInicio, mInicio, hFim, mFim = map(int, entrada)

# Calcula a diferença de horas e minutos
totalH = hFim - hInicio
totalM = mFim - mInicio

# Ajusta os valores caso sejam negativos
if totalH <= 0:
    totalH = 24 + (hFim - hInicio)

if totalM < 0:
    totalM = 60 + (mFim - mInicio)
    totalH -= 1

# Verifica se o início e o fim são iguais
if hInicio == hFim and mInicio == mFim:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print(f'O JOGO DUROU {totalH} HORA(S) E {totalM} MINUTO(S)')