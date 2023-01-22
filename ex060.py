# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))


n = int(input('Digite um número para calcular seu fatorial: '))
contador = n
f = 1
print('Calculando {}! = '.format(n), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    f *= contador
    c -= 1
print('{}'.format(f))
