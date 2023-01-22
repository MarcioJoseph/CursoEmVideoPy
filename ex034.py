sal = float(input('Qual o salário do funcionário? R$: '))
aum15 = sal + sal *15/100
aum10 = sal + sal *10/100

if sal <= 1250:
    print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora'.format(sal, aum15))
if sal > 1250:
    print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora'.format(sal, aum10))

# Primeiro método
salário = float(input('Qual o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salário, novo))
