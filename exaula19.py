pessoas = {'nome': 'Joseph', 'Sexo': 'M', 'idade': 33}
#del pessoas['Sexo']
pessoas['nome'] = 'Bisna'
pessoas['peso'] = 98.5
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['Sigla'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append((estado.copy()))
for e in brasil:
    for k, v in e.items():
        print(v, end='')
    print()