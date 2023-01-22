# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.

times = ('Palmeiras', 'Internacional', 'Fluminense', 'corinthians', 'Flamengo',
         'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América -MG',
         'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
         'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Fluminense está na {times.index("Fluminense")+1}ª posição')
