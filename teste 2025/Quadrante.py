acaba = False

while not acaba:
    x, y = input().split()
    y = int(y)
    x = int(x)
    if x == 0 or y == 0:
        acaba = True
    if x > 0 and y > 0 and not acaba:
        print('primeiro')
    elif x > 0 > y and not acaba:
        print('quarto')
    elif x < 0 and y < 0 and not acaba:
        print('terceiro')
    else:
        if not acaba:
            print('segundo')
