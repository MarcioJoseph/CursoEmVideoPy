#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
pc = randint(0, 10)
print('Sou seu PC...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('\033[34mMais...\033[m Tente mais uma vez.')
        elif jogador > pc:
            print('\033[31mMenos...\033[m Tente mais uma vez.')
print("\033[32mAcertou!\033[m com {} tentativas. Parabéns".format(palpites))
