'''aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'{k} é iqual a {v}')'''


aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if 7 >= aluno['média'] < 10:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
elif 0 <= aluno['média'] < 4.9:
    aluno['situação'] = 'Reprovado'
else:
    print('Notas inválidas')
print('-=' * 30)
for k, v in aluno.items():
    print(f'{k} é iqual a {v}')

