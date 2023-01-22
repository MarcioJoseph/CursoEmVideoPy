from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opções = 0
while opções != 5:
    print('''    [ 1 ] Soma
    [ 2 ] Multiplicar
    [ 3 ] Maior 
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opções = int(input('>>>>>> Qual a sua opção? '))
    if opções == 1:
        soma = n1 + n2
        print("A soma entre {} + {} é {}".format(n1,n2,soma))
    elif opções == 2:
        mult = n1 * n2
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, mult))
    elif opções == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor entre {} e {} é {}'.format(n1, n2, maior))
    elif opções == 4:
        print('Digite novamente os valores: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opções == 5:
        print('Saindo...')
    else:
        print('Opção inválida. Tente novamente')
    sleep(2)
    print('-==-'* 10)
print('Fim do programa! Volte sempre!')
