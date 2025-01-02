import time

tempo = int(input())
horas = tempo // 3600
resto = tempo % 3600
minutos = resto // 60
segundos = resto % 60


print(f'{horas}:{minutos}:{segundos}')

idade = int(input())
ano = idade // 365
rest = idade % 365
mes = rest // 30
dias = rest % 30


print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dias} dia(s)")
