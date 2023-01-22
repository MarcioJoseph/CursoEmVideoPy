#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
from time import sleep
val1 = int(input('Primeiro valor: '))
val2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar 
    [ 2 ] multiplicar 
    [ 3 ] maior 
    [ 4 ] novos números 
    [ 5 ] sair do programa ''')
    opção = int(input('>>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = val1 + val2
        print('\033[32mA soma entre {} + {} é {}\033[m'.format(val1, val2, soma))
    elif opção == 2:
        produto = val1 * val2
        print('\033[33mA multiplicação entre {} x {} é {}\033[m'.format(val1, val2, produto))
    elif opção == 3:
        if val1 > val2:
            maior = val1
        else:
            maior = val2
        print('\033[35mEntre {} e {} o maior valor é {}\033[m'.format(val1, val2, maior))
    elif opção == 4:
        print('\033[34mInforme os números novamente:\033[m ')
        val1 = int(input('Primeiro valor: '))
        val2 = int(input('Segundo valor: '))
    elif opção == 5:
        print("\033[31mFinalizando...\033[m")
    else:
        print('\033[37mOpção inválida. Tente novamente\033[m')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
