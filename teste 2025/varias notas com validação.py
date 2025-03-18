i = 1
j = 0
soma = 0.0
while i != 2:
    nota = float(input())
    if 0.0 <= nota <= 10.0:
        nota /= 2
        soma += nota
        j += 1
    if j == 2:
        print(f'media = {soma:.2f}')
        print('novo calculo (1-sim 2-nao)')
        i = int(input())
        if i == 1 or i == 2:
            aux = True
        else:
            aux = False
        while not aux:
            print('novo calculo (1-sim 2-nao)')
            i = int(input())
            if i == 1 or i == 2:
                aux = True
            else:
                aux = False
        j = 0
        soma = 0
    if nota < 0 or nota > 10:
        print('nota invalida')
