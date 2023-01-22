import math
# fazendo de 'from math import trunc' é uma alternativa q economiza RAM
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))
# print('O valor digitado foi {} e a sua porção inteira é{}'.format(num, trunc(num)))

num = float(input('Digite uma valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))


