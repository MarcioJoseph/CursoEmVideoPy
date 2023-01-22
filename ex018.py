import math
ang = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(ang, seno))
print('O ângulo de {:.1f} tem o COSSENO de {:.2f}'.format(ang, cosseno))
print('O ângulo de {:.1f} tem a TANGENTE de {:.2f}'.format(ang, tang))
