salario = float(input('Qual é o salario do funcionario? R$ '))
aum = salario + (salario*15/100)
print("Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(salario, aum))

preço = float(input('Qual o preço do produto? R$'))
desc = preço - (preço*10/100)
juros = preço + (preço*5/100)

print('O produto custa R${:.2f} a vista, com desconto de 10% ou a prazo com juros de 5 % de R${:.2f}'.format(desc, juros))
