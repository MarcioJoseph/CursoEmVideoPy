from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print("Ao todo tivemos \033[31m{}\033[m pessoas \033[31mmaiores de idade\033[m".format(totmaior))
print('Ao todo tivemos \033[34m{}\033[m pessoas \033[34mmenores de idade\033[m'.format(totmenor))
