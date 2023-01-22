av1 = float(input('Primeira nota: '))
av2 = float(input('Segunda nota: '))
media = (av1 + av2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(av1, av2, media))
if media < 5:
    print('O aluno está reprovado!')
elif media >= 5 and media < 7:
    print('O aluno esta de recuperação')
else media >= 7:
    print('O aluno esta aprovado')

